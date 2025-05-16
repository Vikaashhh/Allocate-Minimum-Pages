class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self, arr, k):
        n = len(arr)  # Total number of books
        
        # Agar students ki sankhya books se zyada hai toh allocation possible nahi
        if k > n:
            return -1

        # Binary search ke liye range set karo
        low = max(arr)        # Har student ko kam se kam ek book deni hai, toh max(arr) lower bound hoga
        high = sum(arr)       # Maximum pages ka upper bound total sum hoga
        ans = -1              # Final answer store karne ke liye

        # Binary search shuru
        while low <= high:
            mid = (low + high) // 2  # Beech ka value nikalo - potential max pages per student

            # Check karo ki yeh mid pages ke hisaab se allocation possible hai ya nahi
            students, total = 1, 0   # Pehle student ko assign karna start karo

            for pages in arr:
                if total + pages > mid:
                    students += 1       # Naya student assign karo
                    total = pages       # Us student ko yeh book dedo
                else:
                    total += pages      # Same student ko pages add karte jao

            if students <= k:
                ans = mid             # Yeh allocation possible hai, answer update karo
                high = mid - 1        # Try karo aur kam pages mein kaam ho jaye
            else:
                low = mid + 1         # Pages badhao, kyunki current mid se kaam nahi ban raha

        return ans  # Minimum of the maximum pages jo kisi student ko assign hongi
