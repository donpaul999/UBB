using System;
using System.ComponentModel.DataAnnotations;

namespace BookABook.Models
{
    public class Book
    {
        [Key]
        public int Id { get; set; }

        [Required]
        public string Name { get; set; }

        [Required]
        public string Author { get; set; }

        [Required]
        public string PublishDate { get; set; }

        [Required]
        public bool IsBooked { get; set; }

        public Guid UserId { get; set; }
        
        [Required]
        public byte[] Image { get; set; }
    }
}
