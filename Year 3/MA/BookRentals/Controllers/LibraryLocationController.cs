using BookABook.DTO;
using BookABook.Services;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace BookABook.Controllers
{
    [Authorize]
    [Route("api/[controller]")]
    [ApiController]
    public class LibraryLocationController : ControllerBase
    {
        private readonly ILibraryLocationService libraryLocationService;

        public LibraryLocationController(ILibraryLocationService libraryLocationService)
        {
            this.libraryLocationService = libraryLocationService;
        }

        [HttpGet]
        public IActionResult GetLibraryLocation()
        {
            var libraryLocation = libraryLocationService.GetLibraryLocation();

            if (libraryLocation == null)
                return NotFound();

            return Ok(libraryLocation);
        }

        [HttpPost]
        public IActionResult SetLibraryLocation(LibraryLocationDto libraryLocation)
        {
            libraryLocationService.SetLibraryLocation(libraryLocation);

            return Ok();
        }
    }
}