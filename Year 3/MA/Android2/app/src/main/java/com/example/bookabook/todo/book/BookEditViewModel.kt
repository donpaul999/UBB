package com.example.bookabook.todo.book

import android.app.Application
import android.util.Log
import androidx.lifecycle.*
import com.example.bookabook.todo.data.BookRepository
import com.example.bookabook.core.TAG
import com.example.bookabook.core.Result
import com.example.bookabook.todo.data.Book
import com.example.bookabook.todo.data.local.TodoDatabase
import kotlinx.coroutines.launch

class BookEditViewModel(application: Application) : AndroidViewModel(application) {
    private val mutableFetching = MutableLiveData<Boolean>().apply { value = false }
    private val mutableCompleted = MutableLiveData<Boolean>().apply { value = false }
    private val mutableException = MutableLiveData<Exception>().apply { value = null }

    val fetching: LiveData<Boolean> = mutableFetching
    val fetchingError: LiveData<Exception> = mutableException
    val completed: LiveData<Boolean> = mutableCompleted

    val bookRepository: BookRepository

    init {
        val bookDao = TodoDatabase.getDatabase(application, viewModelScope).bookDao()
        bookRepository = BookRepository(bookDao)
    }

    fun getBookById(bookId: String): LiveData<Book> {
        Log.v(TAG, "getBookById...")
        return bookRepository.getById(bookId)
    }

    fun saveOrUpdateBook(book: Book) {
        viewModelScope.launch {
            Log.v(TAG, "saveOrUpdateBook...");
            mutableFetching.value = true
            mutableException.value = null
            val result: Result<Book>
            if (book.id > 0) {
                result = bookRepository.update(book)
            } else {
                result = bookRepository.save(book)
            }
            when(result) {
                is Result.Success -> {
                    Log.d(TAG, "saveOrUpdateBook succeeded");
                }
                is Result.Error -> {
                    Log.w(TAG, "saveOrUpdateBook failed", result.exception);
                    mutableException.value = result.exception
                }
            }
            mutableCompleted.value = true
            mutableFetching.value = false
        }
    }
}