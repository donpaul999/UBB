using BookABook.Extensions;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using System.Threading.Tasks;
using BookABook.BookChanges;
using BookABook.BookUpdates;
using BookABook.Models;
using BookABook.Services;

namespace BookABook.Controllers
{
    [Authorize]
    [ApiController]
    [Route("api/[controller]")]
    public class BooksController : ControllerBase
    {
        private const int BAD_REQUEST_STATUS_CODE = 400;

        private readonly IBookService bookService;
        private readonly IBroadcastHandler broadcastHandler;

        public BooksController(IBookService bookService, IBroadcastHandler broadcastHandler)
        {
            this.bookService = bookService;
            this.broadcastHandler = broadcastHandler;
        }

        [HttpPost]
        public IActionResult CreateBook(Book book)
        {
            var createdBook = bookService.Create(book.AttachUserId(this));

            if (createdBook == null) return BadRequest();

            broadcastHandler.Broadcast(ChangeType.Create, createdBook);

            return Ok(createdBook);
        }

        [HttpPut]
        public IActionResult UpdateBook(Book book)
        {
            var updatedBook = bookService.Update(book.AttachUserId(this));

            if (updatedBook == null) return NotFound();

            broadcastHandler.Broadcast(ChangeType.Update, updatedBook);

            return Ok(updatedBook);
        }

        [HttpGet]
        public IActionResult GetAllBooks()
        {
            return Ok(bookService.GetAll());
        }

        [HttpGet("available")]
        public IActionResult GetAvailableBooks()
        {
            return Ok(bookService.GetAvailable());
        }

        [HttpGet("related")]
        public IActionResult GetRelatedBooks()
        {
            return Ok(bookService.GetRelated());
        }

        [HttpDelete("{id}")]
        public IActionResult DeleteBooks(int id)
        {
            var deletedBook = bookService.Delete(id);

            if (deletedBook == null) return NotFound();

            broadcastHandler.Broadcast(ChangeType.Delete, deletedBook);

            return Ok(deletedBook);
        }

        [HttpGet("changes")]
        public async Task GetUpdatesAsync()
        {
            if (!HttpContext.WebSockets.IsWebSocketRequest)
            {
                HttpContext.Response.StatusCode = BAD_REQUEST_STATUS_CODE;
                return;
            }

            using var webSocket = await HttpContext.WebSockets.AcceptWebSocketAsync("access_token");

            await broadcastHandler.AddConnection(webSocket);
        }
    }
}
