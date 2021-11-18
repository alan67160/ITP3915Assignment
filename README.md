# ITP3915 - Programming Fundamentals Assignment
A inventory management system

[Download](https://github.com/alan67160/ITP3915Assignment)

# Requirement
- [x] This Inventory Management System has 4 functions. Users are allowed to borrow item(s), return item(s), Display item(s) borrowed by particular user, and Display all records
  - [x] show main menu
    - [x] borrow item(s)
    - [x] return item(s)
    - [x] Display item(s) borrowed by particular user
    - [x] Display all records
  - [x] ask for select functions
- [ ] Only 5 item(s) are allowed to borrow or return in this system
- [x] To borrow an item, user is required to input the item number to borrow, the number of quantity to borrow (given that the quantity left satisfy user's request), and the borrower's name
  - [x] show `item list` with `remaining quantity`
  - [x] ask `item no`
  - [x] ask `quantity`
  - [x] quantity check
  - [x] ask `borrower's name`
  - [x] show `borrow record` of the `borrower` after `borrow`
- [x] To return an item, user is required to input the borrower's name, the item number to return, the number of quantity to return (given that the quantity to return is small than or equals to the quantity borrowed)
  - [x] ask `borrower's name`
  - [x] show `borrow record` of the `the borrower`
  - [x] ask `item no`
  - [x] ask `quantity`
  - [x] quantity check
  - [x] show `borrow record` of the `borrower` after `return`
- [x] The borrower's name, quantity borrowed (or returned), item name, and list of item(s) this borrower's currently borrowed would be displayed for every successful borrow or return action
- [x] The list of allowed borrowers are stored in a text file named "borrowers.txt"
  - [x] read `borrowers.txt`
  - [x] write to `user_list`

# Test Plan
| ID   | Test Case Name  | Procedure | Expected Output | Result |
| :--: | --------------- | --------- | --------------- | ------ |
| 01 | Main menu | In the inventory management main menu, input `4` or `-1` | An error message "Invalid input for choice" should be displayed and will ask the user to input function number again | Pass / ~~Fail~~ |
|  |  | In the inventory management main menu, input `a` | An error message "Invalid input for choice" should be displayed and will ask the user to input function number again | Pass / ~~Fail~~ |
| 02 | Return item - item no | In the inventory management return item no, input `99` or `-99` | An error message "you can't select a non-exist item" should be displayed and will ask the user to input function number again | Pass / ~~Fail~~ |
|  |  | In the inventory management return item no, input `b` | An error message "Invalid value for item no." should be displayed and will ask the user to input function number again | Pass / ~~Fail~~ |
| 03 | Return item - quantity | In the inventory management return quantity, input `0` or `-99` | An error message "You can't return less then 1 item." should be displayed and will ask the user to input function number again | Pass / ~~Fail~~ |
|  |  | In the inventory management return quantity, input `b` | An error message "Invalid value for item no." should be displayed and will ask the user to input function number again | Pass / ~~Fail~~ |
|  |  | In the inventory management return quantity, input `4`, but the user only borrowed `3` | An error message "Your return quantity is over your borrow record." should be displayed and will ask the user to input function number again | Pass / ~~Fail~~ |
| 04 | borrow item - item no | In the inventory management borrow item no, input `99` or `-99` | An error message "you can't select a non-exist item" should be displayed and will ask the user to input function number again | Pass / ~~Fail~~ |
|  |  | In the inventory management borrow item no, input `b` | An error message "Invalid value for item no." should be displayed and will ask the user to input function number again | Pass / ~~Fail~~ |
|  |  | In the inventory management borrow item no, input `1`, but item `1` is out of stock  | An error message "The selected item is currently out of stock." should be displayed and will ask the user to input function number again | Pass / ~~Fail~~ |
| 05 |  |  |  | Pass / ~~Fail~~ |
| 06 |  |  |  | Pass / ~~Fail~~ |
| 07 |  |  |  | Pass / ~~Fail~~ |
| 08 |  |  |  | Pass / ~~Fail~~ |
| 09 |  |  |  | Pass / ~~Fail~~ |
| 10 |  |  |  | Pass / ~~Fail~~ |
