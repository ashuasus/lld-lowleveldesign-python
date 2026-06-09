from .balance import Balance


class BalanceSheetController:
    def update_user_expense_balance_sheet(self, expense_paid_by, splits, total_expense_amount):
        # update the total amount paid of the expense paid by user
        paid_by_user_expense_sheet = expense_paid_by.get_user_expense_balance_sheet()
        paid_by_user_expense_sheet.set_total_payment(paid_by_user_expense_sheet.get_total_payment() + total_expense_amount)

        for split in splits:
            user_owe = split.get_user()
            owe_user_expense_sheet = user_owe.get_user_expense_balance_sheet()
            owe_amount = split.get_amount_owe()

            if expense_paid_by.get_user_id() == user_owe.get_user_id():
                paid_by_user_expense_sheet.set_total_your_expense(paid_by_user_expense_sheet.get_total_your_expense() + owe_amount)
            else:
                # update the balance of paid user
                paid_by_user_expense_sheet.set_total_you_get_back(paid_by_user_expense_sheet.get_total_you_get_back() + owe_amount)

                if user_owe.get_user_id() in paid_by_user_expense_sheet.get_user_vs_balance():
                    user_owe_balance = paid_by_user_expense_sheet.get_user_vs_balance()[user_owe.get_user_id()]
                else:
                    user_owe_balance = Balance()
                    paid_by_user_expense_sheet.get_user_vs_balance()[user_owe.get_user_id()] = user_owe_balance

                user_owe_balance.set_amount_get_back(user_owe_balance.get_amount_get_back() + owe_amount)

                # update the balance sheet of owe user
                owe_user_expense_sheet.set_total_you_owe(owe_user_expense_sheet.get_total_you_owe() + owe_amount)
                owe_user_expense_sheet.set_total_your_expense(owe_user_expense_sheet.get_total_your_expense() + owe_amount)

                if expense_paid_by.get_user_id() in owe_user_expense_sheet.get_user_vs_balance():
                    user_paid_balance = owe_user_expense_sheet.get_user_vs_balance()[expense_paid_by.get_user_id()]
                else:
                    user_paid_balance = Balance()
                    owe_user_expense_sheet.get_user_vs_balance()[expense_paid_by.get_user_id()] = user_paid_balance

                user_paid_balance.set_amount_owe(user_paid_balance.get_amount_owe() + owe_amount)

    def show_balance_sheet_of_user(self, user):
        print("---------------------------------------")
        print("Balance sheet of user : " + user.get_user_id())
        user_expense_balance_sheet = user.get_user_expense_balance_sheet()
        print("TotalYourExpense: " + str(user_expense_balance_sheet.get_total_your_expense()))
        print("TotalGetBack: " + str(user_expense_balance_sheet.get_total_you_get_back()))
        print("TotalYourOwe: " + str(user_expense_balance_sheet.get_total_you_owe()))
        print("TotalPaymnetMade: " + str(user_expense_balance_sheet.get_total_payment()))
        for user_id, balance in user_expense_balance_sheet.get_user_vs_balance().items():
            print("userID:" + user_id + " YouGetBack:" + str(balance.get_amount_get_back()) + " YouOwe:" + str(balance.get_amount_owe()))
        print("---------------------------------------")
