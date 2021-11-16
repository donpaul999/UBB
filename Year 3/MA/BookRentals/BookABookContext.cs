using BookABook.Authentication;
using BookABook.DTO;
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
        public DbSet<LibraryLocation> LibraryLocations { get; set; }
        
        protected override void OnModelCreating(ModelBuilder builder)
        {
            builder.Entity<LibraryLocation>()
                .Property(location => location.Latitude)
                .HasPrecision(28, 15);
            builder.Entity<LibraryLocation>()
                .Property(location => location.Longitude)
                .HasPrecision(28, 15);

            base.OnModelCreating(builder);
        }
    }
}
