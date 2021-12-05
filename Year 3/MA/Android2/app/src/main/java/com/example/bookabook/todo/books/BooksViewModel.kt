package com.example.bookabook.todo.books

import android.app.Application
import android.util.Log
import androidx.lifecycle.*
import com.example.bookabook.todo.data.BookRepository
import com.example.bookabook.core.TAG
import com.example.bookabook.core.Result
import com.example.bookabook.todo.data.Book
import com.example.bookabook.todo.data.local.TodoDatabase
import kotlinx.coroutines.launch
class BookListViewModel(application: Application) : AndroidViewModel(application) {
    private val mutableLoading = MutableLiveData<Boolean>().apply { value = false }
    private val mutableException = MutableLiveData<Exception>().apply { value = null }

    val books: LiveData<List<Book>>
    val loading: LiveData<Boolean> = mutableLoading
    val loadingError: LiveData<Exception> = mutableException

    val bookRepository: BookRepository

    init {
        val bookDao = TodoDatabase.getDatabase(application, viewModelScope).bookDao()
        bookRepository = BookRepository(bookDao)
        books = bookRepository.books
    }

    fun refresh() {
        viewModelScope.launch {
            Log.v(TAG, "refresh...");
            mutableLoading.value = true
            mutableException.value = null
            when (val result = bookRepository.refresh()) {
                is Result.Success -> {
                    Log.d(TAG, "refresh succeeded");
                }
                is Result.Error -> {
                    Log.w(TAG, "refresh failed", result.exception);
                    mutableException.value = result.exception
                }
            }
            mutableLoading.value = false
        }
    }
}
