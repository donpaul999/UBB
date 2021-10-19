using BookABook.Authentication;
using BookABook.Models;
using Microsoft.AspNetCore.Identity.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore;

namespace BookABook
{
    public class BookABookContext : IdentityDbContext<ApplicationUser>
    {
        public BookABookContext(DbContextOptions<BookABookContext> options) : base(options)
        {
        }

        public DbSet<Book> Books { get; set; }
    }
}
