import pandas as pd
import pytest
import datatest as dt
import edit as clients
import people as people

df = pd.read_csv("data/client_data.csv")


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

def test_view_negative_clients():
    """Tests that the length of view_negative is == 12"""
    All = people.AllClients()
    assert len(All.view_negative()) == 12

def test_columns():
    """Tests column names validate"""
    dt.validate(df.columns,
                {'First name', 'Last name', 'Title', 'Pronoun', 'Account Number', 'Date of birth', 'Occupation',
                 'Account balance', 'overdraft limit'}, )


