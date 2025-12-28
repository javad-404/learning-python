def audit_log(func):
    def wrapper(*args, **kwargs):
        print("[SYSTEM AUDIT] ation started")
        result = func(*args, **kwargs)
        return result
    return wrapper
        
class ArchiveSystem:
    def __init__(self):
        self.letters = []
    
    @audit_log
    def register_letter(self, text):
        if not text.strip():
            raise ValueError("Text cant be empty")
        
        self.letters.append(text)
        print("Letter registered successfully")
        
if __name__ == "__main__":
    my_archive = ArchiveSystem()
    print("--- Test 1: Normal Letter ---")
    my_archive.register_letter("darkhast asphalt")
    print("\n--- Test 2: Empty Letter ---")
    try:
        my_archive.register_letter("  ")
    except Exception as e:
        print(f"Caught an error: {e}")
    
    
    
        