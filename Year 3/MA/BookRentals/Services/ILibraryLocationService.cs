using BookABook.DTO;

namespace BookABook.Services
{
    public interface ILibraryLocationService
    {
        LibraryLocationDto GetLibraryLocation();

        void SetLibraryLocation(LibraryLocationDto libraryLocationDto);
    }
}