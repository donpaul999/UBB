package com.example.bookabook.todo.data

import android.util.Log
import androidx.lifecycle.LiveData
import com.example.bookabook.core.TAG
import com.example.bookabook.core.Result
import com.example.bookabook.todo.data.local.BookDao
import com.example.bookabook.todo.data.remote.BookApi

class BookRepository(private val bookDao: BookDao) {
    val books = bookDao.getAll()

    suspend fun refresh(): Result<Boolean> {
        try {
            val books = BookApi.service.find()
            for (book in books) {
                bookDao.insert(book)
            }
            return Result.Success(true)
        } catch (e: Exception) {
            return Result.Error(e)
        }
    }

    fun getById(bookId: String): LiveData<Book> {
        return bookDao.getById(bookId)
    }

    suspend fun save(book: Book): Result<Book> {
        try {
            val createdBook = BookApi.service.create(book)
            bookDao.insert(createdBook)
            return Result.Success(createdBook)
        } catch (e: Exception) {
            return Result.Error(e)
        }
    }

    suspend fun update(book: Book): Result<Book> {
        try {
            val updatedBook = BookApi.service.update(book)
            bookDao.update(updatedBook)
            return Result.Success(updatedBook)
        } catch (e: Exception) {
            return Result.Error(e)
        }
    }
}