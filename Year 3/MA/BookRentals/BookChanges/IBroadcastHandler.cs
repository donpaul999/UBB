using System.Net.WebSockets;
using System.Threading.Tasks;
using BookABook.BookChanges;

namespace BookABook.BookUpdates
{
    public interface IBroadcastHandler
    {
        Task AddConnection(WebSocket webSocket);

        Task Broadcast<T>(ChangeType type, T payload);
    }
}
