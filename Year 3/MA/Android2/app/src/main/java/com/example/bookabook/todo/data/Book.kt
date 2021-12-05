package com.example.bookabook.todo.data

import androidx.room.ColumnInfo
import androidx.room.Entity
import androidx.room.PrimaryKey
@Entity(tableName = "Books")
data class Book(
    @PrimaryKey @ColumnInfo(name = "Id") val id: Int,
    @ColumnInfo(name = "Name") var name: String,
    @ColumnInfo(name = "Author") var author: String,
    @ColumnInfo(name = "PublishDate") var publishDate: String,
    @ColumnInfo(name = "isBooked") var isBooked: Boolean,
) {
    override fun toString(): String = "$id, $name, $author, $publishDate" + if (isBooked) " yes" else " no"
}