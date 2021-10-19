using BookABook.Extensions;
using Microsoft.AspNetCore.Http;
using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.Linq;
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

        public List<Book> GetRelated()
        {
            var userId = httpContextAccessor.GetUserId();

            return context.Books.Where(book => book.UserId == userId).ToList();
        }

        public Book Update(Book bookUpdate)
        {
            var initialBook = context.Books
                .Where(book => book.Id == bookUpdate.Id)
                .AsNoTracking()
                .FirstOrDefault();

            if (initialBook == null || initialBook.UserId != bookUpdate.UserId)
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
    }
}
