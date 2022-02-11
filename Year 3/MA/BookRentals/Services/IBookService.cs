﻿using System.Collections.Generic;
using BookABook.BookChanges;
using BookABook.Models;

namespace BookABook.Services
{
    public interface IBookService
    {
        List<Book> GetAll();

        List<Book> GetAvailable();

        List<Book> GetRelated(string searchKeyword, bool? isBooked, int from, int count);

        Book Create(Book book);

        Book Update(Book book);

        Book Delete(int id);

        Book GetBook(int id);
        
        List<IdMap> MapChanges(List<Change<Book>> carChanges);
    }
}