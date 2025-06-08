def make_shirt(size="M", text="Welcome to the Jungle", color="White", style="Unisex"):
    print(f"--- Shirt Details ---")
    print(f"Size   : {size}")
    print(f"Text   : \"{text}\"")
    print(f"Color  : {color}")
    print(f"Style  : {style}")
    print(f"----------------------\n")

# Example usage
make_shirt("L", "Adventure Awaits", "Black", "Men's Fit")
make_shirt()  # uses default values
