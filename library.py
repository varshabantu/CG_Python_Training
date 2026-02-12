import logging

logging.basicConfig(
    filename="library.log",
    level=logging.INFO,
    format="%(asctime)s-%(levelname)s-%(message)s"
)
class LibraryBook:
    fine_per_day=2
    def __init__(self,book_id,title,days_late=0):
        self.book_id=book_id
        self.title=title
        self.days_late=days_late
        self.issued=False
        logging.info("LibraryBook obj created:%s",self.title)
    def issue_book(self):
        if self.issued:
            logging.warning("Book already issued:%s",self.title)
        else:
            self.issued=True
            logging.info("Book issued successfully:%s",self.title)
    def return_book(self):
        if not self.issued:
            logging.warning("Book is not issued, cannot return : %s", self.title)
        else:
            self.issued = False
            logging.info("Book returned successfully : %s", self.title)
    def calculate_fine(self):
        if self.days_late <= 0:
            logging.info("No fine for book : %s", self.title)
            return 0
        fine = self.days_late * LibraryBook.fine_per_day
        logging.info(
            "Fine calculated for book %s : %d",
            self.title,
            fine
        )
        return fine
    @classmethod
    def update_fine_per_day(cls, new_fine):
        cls.fine_per_day = new_fine
        logging.info("Fine per day updated to : %d", new_fine)

b1 = LibraryBook(101,"Python Programming", 3)
b1.issue_book()
fine_amount = b1.calculate_fine()
logging.info("Returned fine amount : %d", fine_amount)
LibraryBook.update_fine_per_day(5)
fine_amount = b1.calculate_fine()
logging.info("Returned fine amount after update : %d", fine_amount)
b1.return_book()
    