using BookABook.Extensions;
using Microsoft.AspNetCore.Http;
using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.Linq;
using BookABook.BookChanges;
using BookABook.Models;

namespace BookABook.Services
{
    public class BookService : IBookService
    {
        private readonly BookABookContext context;
        private readonly IHttpContextAccessor httpContextAccessor;

        public BookService(BookABookContext context, IHttpContextAccessor httpContextAccessor)
        {
            this.context = context;
            this.httpContextAccessor = httpContextAccessor;
        }

        public Book Create(Book book)
        {
            book.UserId = httpContextAccessor.GetUserId();
            try
            {
                context.Books.Add(book);
                context.SaveChanges();
            }
            catch (Exception)
            {
                return null;
            }

            return book;
        }

        public List<Book> GetAll()
        {
            return context.Books.ToList();
        }

        public List<Book> GetAvailable()
        {
            var userId = httpContextAccessor.GetUserId();

            return context.Books.Where(book => book.UserId != userId).ToList();
        }

        public List<Book> GetRelated(string searchKeyword, bool? isBooked, int from, int count)
        {
            var userId = httpContextAccessor.GetUserId();

            var books = context.Books.Where(car => car.UserId == userId);

            if (!string.IsNullOrWhiteSpace(searchKeyword))
                books = books.Where(book =>
                    book.Name.ToLower().Contains(searchKeyword.ToLower()) ||
                    book.Author.ToLower().Contains(searchKeyword.ToLower()));

            if (isBooked != null)
                books = books.Where(book => book.IsBooked == isBooked);

            if (count < 1)
                return books.ToList();

            return books.Skip(from)
                .Take(count)
                .ToList();
        }

        public Book Update(Book bookUpdate)
        {

            if (bookUpdate.UserId == Guid.Empty)
                bookUpdate.UserId = httpContextAccessor.GetUserId();
            
            var initialBook = context.Books
                .Where(book => book.Id == bookUpdate.Id)
                .AsNoTracking()
                .FirstOrDefault();
            
            if (initialBook == null)
                return null;

            context.Books.Update(bookUpdate);
            context.SaveChanges();

            return bookUpdate;
        }

        public Book Delete(int id)
        {
            var book = context.Books.Find(id);
            var userId = httpContextAccessor.GetUserId();

            if (book == null || book.UserId != userId)
                return null;
            
            context.Remove(book);
            context.SaveChanges();
            
            return book;
        }
        
        public Book GetBook(int id)
        {
            var book = context.Books.Find(id);
            var userId = httpContextAccessor.GetUserId();

            if (book == null || book.UserId != userId)
                return null;

            return book;
        }
        
        public List<IdMap> MapChanges(List<Change<Book>> bookChanges)
        {
            var bookIdMapping = new List<IdMap>();

            foreach (var bookChange in bookChanges)
            {
                var idMap = MapChange(bookChange, bookIdMapping);
                if (idMap != null)
                    bookIdMapping.Add(idMap);
            }

            return bookIdMapping;
        }

        private IdMap MapChange(Change<Book> bookChange, List<IdMap> idMapping)
        {
            var book = bookChange.Payload;

            return bookChange.Type switch
            {
                ChangeType.Create => MapCreateChange(book),
                ChangeType.Update => MapUpdateChange(book, idMapping),
                ChangeType.Delete => MapDeleteChange(book),
                _ => null
            };
        }

        private IdMap MapCreateChange(Book book)
        {
            if (book.Id > 0)
                return null;

            var initialId = book.Id;
            book.Id = 0;
            var addedCar = Create(book);

            return new() {
                From = initialId,
                To = addedCar.Id
            };
        }

        private IdMap MapUpdateChange(Book book, List<IdMap> idMapping)
        {
            if (book.Id > 0)
            {
                Update(book);
                return null;
            }

            var actualId = idMapping.FirstOrDefault(mapping => mapping.From == book.Id);
            if (actualId == null)
                return null;

            book.Id = actualId.To;
            Update(book);
            return null;
        }

        private IdMap MapDeleteChange(Book book)
        {
            if (book.Id > 0)
                Delete(book.Id);

            return null;
        }
    }
}
