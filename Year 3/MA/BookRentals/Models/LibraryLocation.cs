using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace BookABook.Models
{
    public class LibraryLocation
    {
        [Key, ForeignKey("User")]
        public Guid UserId { get; set; }

        public decimal Latitude { get; set; }

        public decimal Longitude { get; set; }
    }
}