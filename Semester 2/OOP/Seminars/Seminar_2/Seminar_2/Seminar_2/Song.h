#pragma once
#include <string>

class Duration {
private:
	int minutes, seconds;
	;
public:
	Duration(int minutes = 0, int seconds = 0);
};

class Song
{
private:
	std::string artist;
	std::string title;
	Duration duration;
public:
	Song();
	Song(const std::string& artist, const std::string& title, Duration duration);
	std::string getArtist() const;
	std::string getTitle() const;
	Duration getDuration() const;
	void setArtist(const std::string& artistSet);
};

