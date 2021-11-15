class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        total_seats = [0] * (n + 1)
        
        for i, j, seat in bookings:
            total_seats[i-1] += seat
            total_seats[j] -= seat
        
        for k in range(1, n):
            total_seats[k] += total_seats[k-1]
        
        return total_seats[: n]
