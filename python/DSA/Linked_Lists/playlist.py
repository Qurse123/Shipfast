class Song:
    """Node class representing a song in the playlist"""
    def __init__(self, title, artist): ## this is what defines our "node" which is a song 
        self.title = title
        self.artist = artist
        self.next = None ## this does not point to another node hence the head of this linked list empty or "none"
    
    def __str__(self):
        return f"{self.title} - {self.artist}" ## used when someone wants to see a song object as text show it as "title - artist"

class Playlist:
    """Linked list implementation of a music playlist"""
    def __init__(self):
        self.head = None ## no songs are currently at the head of this linked list 
        self.current = None  # Points to currently playing song --> in this case it points to nothing
        self.size = 0 ## how many songs are in the playlist
    

    def add_song(self, title, artist):
        """Add a new song to the end of the playlist"""
        new_song = Song(title, artist) ## "Song" inputs are just strings that cannot be connected hence you creaate new_song defined as Song(title, artist) so that each added song with its indivual strings are now a node that you can connect

        if self.head is None: ## if there is no head to this linked list
            self.head = new_song ## if there are no songs in the playlsit already you make the current song being added the head of the list
            self.current = new_song 
            self.size = 1
        else:
            Song = self.head ## here we define song as the head of our list 
            while Song.next is not None: # while the next node called song.next is not empty 
                Song = Song.next ## song will be connected to the next song node or song.next until this while loop condition fails when it fails ->
            Song.next = new_song ## when song.next is none song.next will now be new song, the song the user added
            self.size += 1 ## how many songs in the playlist will increment by 1 as the user can only input 1 song at a time


    def view_playlist(self):
        """Display all songs in the playlist"""
        # TODO(human): Implement this method
        # Hint: Traverse from head and print each song with a number
        pass
    
    def search_song(self, title):
        """Search for a song by title in the playlist"""
        # TODO(human): Implement this method
        # Hint: Traverse and compare titles, return True/False
        pass
    
    def remove_song(self, title):
        """Remove a song from the playlist by title"""
        # TODO(human): Implement this method
        # Hint: Handle head deletion separately, then traverse to find and unlink
        pass
    
    def play_next(self):
        """Move to the next song in playlist"""
        # TODO(human): Implement this method
        # Hint: Move current pointer to current.next, handle wraparound
        pass
    
    def play_previous(self):
        """Move to the previous song in playlist"""
        # TODO(human): Implement this method
        # Hint: This is tricky with singly linked list - traverse from head to find previous
        pass
    
    def get_current_song(self):
        """Get the currently playing song"""
        
        pass


def main():
    """Main program loop"""
    playlist = Playlist()
    
    while True:
        print("\n=== Music Playlist Manager ===")
        print("1. Add Song")
        print("2. View Playlist") 
        print("3. Play Next")
        print("4. Play Previous")
        print("5. Remove Song")
        print("6. Search Song")
        print("7. Current Song")
        print("8. Quit")
        
        choice = input("\nEnter your choice (1-8): ").strip()
        
        if choice == '1':
            title = input("Enter song title: ").strip()
            artist = input("Enter artist: ").strip()
            playlist.add_song(title, artist)
            print(f"Added: {title} - {artist}")
            
        elif choice == '2':
            playlist.view_playlist()
            
        elif choice == '3':
            playlist.play_next()
            print(f"Now playing: {playlist.get_current_song()}")
            
        elif choice == '4':
            playlist.play_previous()
            print(f"Now playing: {playlist.get_current_song()}")
            
        elif choice == '5':
            title = input("Enter song title to remove: ").strip()
            if playlist.remove_song(title):
                print(f"Removed: {title}")
            else:
                print(f"Song '{title}' not found")
                
        elif choice == '6':
            title = input("Enter song title to search: ").strip()
            if playlist.search_song(title):
                print(f"Found: {title}")
            else:
                print(f"Song '{title}' not found")
                
        elif choice == '7':
            print(f"Currently playing: {playlist.get_current_song()}")
            
        elif choice == '8':
            print("Thanks for using Music Playlist Manager!")
            break
            
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()