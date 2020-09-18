class Editor:
    def view_document(self):
        print("view")
    def edit_document(self):
        print("This method is unavailable for the free version of the editor")

class ProEditor(Editor):
    def edit_document(self):
        print("edit")
        
def main():
    
    print("Enter lisence key...")
    
    l_key = input()
    
    if l_key == "12A34B":
        editor = ProEditor()
    else:
        editor = Editor()
    
    editor.view_document()
    editor.edit_document()
    
if __name__== '__main__':
    main()
