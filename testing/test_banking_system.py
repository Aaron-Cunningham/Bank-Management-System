import pandas as pd
import pytest
import datatest as dt
import banking_system.edit as clients
import banking_system.people as people

df = pd.read_csv("data/client_data.csv")
test_df = pd.read_csv("testing/client_data_test.csv")
All = people.AllClients()


def test_TypeError_for_account_number():
    """Tests isinstance account has bad values and raises TypeError
    >> account = str
    """
    with pytest.raises(TypeError):
        client_to_be_edited = clients.Edit(account="1898")
        client_to_be_edited.set_first_name()


def test_add_client_TypeError():
    """Tests add.account method for bad values
       >> Test value account = "5500"
       >> Test value account balance = "6857489"
       >> Test value account overdraft = "-40000"
    """
    with pytest.raises(TypeError):
        Jeff_Bazos = clients.Add("Jeff", "Bezos", "Mr", "Male", "5500", "01/12/1964", "CEO of Amazon", "6857489",
                                 "-40000")
        Jeff_Bazos.add_account()


def test_new_first_name_TypeError():
    """Tests except method for new_name which only allows strings
       >> Test value = 123
    """
    with pytest.raises(TypeError):
        client_to_be_edited = clients.Edit(account=1898)
        client_to_be_edited.set_first_name(123)


def test_new_last_name_TypeError():
    """Tests except method for new_name which only allows strings
       >> Test value = 123
    """
    with pytest.raises(TypeError):
        client_to_be_edited = clients.Edit(account=1898)
        client_to_be_edited.set_last_name(123)


def test_new_occupation_TypeError():
    """Tests except method for new_name which only allows strings
       >> Test value = 123
    """
    with pytest.raises(TypeError):
        client_to_be_edited = clients.Edit(account=1898)
        client_to_be_edited.set_occupation(123)


def test_deposit_TypeError():
    """
    This test will check if the type error works for the deposit method
    """
    with pytest.raises(TypeError):
        known_user = people.Users("Aaron", "Cunningham", "01/29/1999")
        known_user.deposit("1")


def test_withdraw_TypeError():
    """
    This test will check if the type error works for the withdraw method
    """
    with pytest.raises(TypeError):
        known_user = people.Users("Aaron", "Cunningham", "01/29/1999")
        known_user.withdraw("1")


def test_columns():
    """Tests column names validate"""

    dt.validate(df.columns,
                {'First name', 'Last name', 'Title', 'Pronoun', 'Account Number', 'Date of birth', 'Occupation',
                 'Account balance', 'overdraft limit'}, )


def test_view_negative_clients():
    len(df.loc[df['Account balance'] < 0]) == 12


def test_search_by_name_pass():
    """
    Test searches for a known client in the CSV file.
    Test will pass if the known user is found
    """
    known_user = people.Users("Aaron", "Cunningham", "01/29/1999")
    if known_user.get_account_details.empty:
        pytest.fail()


def test_search_by_name_fail():
    """
    Test searches for an unknown client in the database.
    Test will pass if no user is found
    """
    unknown_user = people.Users("Freddie", "Mercury", "09/05/1946")
    if unknown_user.get_account_details.empty:
        pass
    else:
        pytest.fail()


def test_search_by_account_num_pass():
    """
    This test checks that an account can
    be found in the CSV file when inputting correct data.
    Test will pass if an account is found
    """
    known_user = clients.Edit(account=1898)
    if known_user.get_account.empty:
        pytest.fail()


def test_search_by_account_num_fail():
    """
    This test checks that when wrong account number
    is inputted it won't return any data.
    Test will pass if no data is found.
    """
    unknown_user = clients.Edit(account=1)
    if unknown_user.get_account.empty:
        pass
    else:
        pytest.fail()


def test_view_negative_clients_size_pass():
    """
    Tests that the length of negative accounts in  is == 12
    """
    negative = test_df.loc[test_df['Account balance'] < 0]

    assert len(negative) == 12


def test_view_negative_clients_size_fail():
    """
    This test checks if an Assertion Error is caught
    when wrong negative client len is inputted
    """
    with pytest.raises(AssertionError):
        negative = test_df.loc[test_df['Account balance'] < 0]
        assert len(negative) == 13


def test_df_size_pass():
    """
    This test checks the len of the CSV file is correct.
    """
    assert len(test_df) == 125


def test_df_size_fail():
    """
    This test checks the assertion error is caught
    when wrong CSV len is entered
    """
    with pytest.raises(AssertionError):
        assert len(test_df) == 500
