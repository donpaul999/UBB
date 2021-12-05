package com.example.bookabook.todo.data.local

import androidx.lifecycle.LiveData
import androidx.room.*
import com.example.bookabook.todo.data.Book

@Dao
interface BookDao {
    @Query("SELECT * from Books ORDER BY id ASC")
    fun getAll(): LiveData<List<Book>>

    @Query("SELECT * FROM Books WHERE id=:id ")
    fun getById(id: String): LiveData<Book>

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insert(book: Book)

    @Update(onConflict = OnConflictStrategy.REPLACE)
    suspend fun update(book: Book)

    @Query("DELETE FROM Books")
    suspend fun deleteAll()
}