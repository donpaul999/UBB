using System.Linq;
using BookABook.DTO;
using BookABook.Extensions;
using BookABook.Models;
using Microsoft.AspNetCore.Http;

namespace BookABook.Services
{
    public class LibraryLocationService : ILibraryLocationService
    {
        private readonly BookABookContext context;
        private readonly IHttpContextAccessor httpContextAccessor;

        public LibraryLocationService(
            BookABookContext context,
            IHttpContextAccessor httpContextAccessor)
        {
            this.context = context;
            this.httpContextAccessor = httpContextAccessor;
        }

        public LibraryLocationDto GetLibraryLocation()
        {
            var userId = httpContextAccessor.GetUserId();
            var libraryLocation = context.LibraryLocations
                .FirstOrDefault(location => location.UserId == userId);

            if (libraryLocation == null)
                return null;

            return new LibraryLocationDto(libraryLocation);
        }

        public void SetLibraryLocation(LibraryLocationDto parkLocationDto)
        {
            var libraryLocation = new LibraryLocation
            {
                Latitude = parkLocationDto.Latitude,
                Longitude = parkLocationDto.Longitude,
                UserId = httpContextAccessor.GetUserId()
            };

            var exists = context.LibraryLocations
                .Any(location => location.UserId == libraryLocation.UserId);

            if (exists)
                context.Update(libraryLocation);
            else
                context.Add(libraryLocation);
            context.SaveChanges();
        }
    }
}