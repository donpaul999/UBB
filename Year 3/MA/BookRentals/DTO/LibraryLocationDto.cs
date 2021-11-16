using BookABook.Models;

namespace BookABook.DTO
{
    public class LibraryLocationDto
    {
        public decimal Latitude { get; set; }

        public decimal Longitude { get; set; }

        public LibraryLocationDto() { }

        public LibraryLocationDto(decimal latitude, decimal longitude)
        {
            Latitude = latitude;
            Longitude = longitude;
        }

        public LibraryLocationDto(LibraryLocation libraryLocation)
        {
            Latitude = libraryLocation.Latitude;
            Longitude = libraryLocation.Longitude;
        }
    }
}