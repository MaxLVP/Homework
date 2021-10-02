
class Pagination():
    
    def __init__(self, text, num_of_symb):
        self.text = text
        self.num_of_symb = num_of_symb
        
    def page_count(self):
        return((len(self.text)//self.num_of_symb) +1 )
    
    def item_count(self):
        return(len(self.text))
    
    def count_items_on_page(self, symb_on_page):
        if symb_on_page < ((len(self.text)//self.num_of_symb)  ):
            return self.num_of_symb
        elif symb_on_page == ((len(self.text)//self.num_of_symb) ):
            return(len(self.text) - (self.num_of_symb*(len(self.text)//self.num_of_symb)+1 ))
        else:
            return("Invalid index. Page is missing.")
