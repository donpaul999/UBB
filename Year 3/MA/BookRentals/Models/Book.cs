using System;
using System.ComponentModel.DataAnnotations;

namespace BookABook.Models
{
    public class Book
    {
        [Key]
        public int Id { get; set; }

        public string Name { get; set; }

        public string Author { get; set; }

        public string PublishDate { get; set; }

        public bool IsBooked { get; set; }

        public Guid UserId { get; set; }
        
        public byte[] Image { get; set; }
    }
}
