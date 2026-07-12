class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        for index, ticket in enumerate(tickets):
            start, end = ticket
            adj[start].append((end, index))

        for city in adj:
            adj[city].sort()

        path = ["JFK"]
        visited = set()

        def dfs(city):
            if len(visited) == len(tickets):
                return True

            for next_city, ticket_index in adj[city]:
                if ticket_index not in visited:
                    visited.add(ticket_index)
                    path.append(next_city)

                    if dfs(next_city):
                        return True

                    visited.remove(ticket_index)
                    path.pop()

            return False

        dfs("JFK")
        return path