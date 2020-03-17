#include "Song.h"

Duration::Duration(int minutes, int seconds)
{
	this->minutes = minutes;
	this->seconds = seconds;
}

Song::Song()
{
	artist = "";
	title = "";
	duration = Duration(0, 0);
}

Song::Song(const std::string& artist, const std::string& title, Duration duration){
	this->artist = artist;
	this->title = title;
	this->duration = duration;
}

std::string Song::getArtist() const
{
	return artist;
}

std::string Song::getTitle() const
{
	return title;
}

Duration Song::getDuration() const
{
	return duration;
}

void Song::setArtist(const std::string& artistSet) {
	artist = artistSet;
}