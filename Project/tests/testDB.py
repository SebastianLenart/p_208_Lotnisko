import pytest
import sys
import os
sys.path.append(os.path.abspath("/home/sebastian/GitHub/p_208_Lotnisko/Project"))
from unittest.mock import patch




import pytest
from unittest.mock import patch, MagicMock

@patch('psycopg2.connect')
def test_add_data_plane(mock_connect):
    # Mockowanie połączenia i kursora
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_connect.return_value = mock_conn
    mock_conn.cursor.return_value.__enter__.return_value = mock_cursor

    # Dane wejściowe
    data = {
        "number_flight": 1,
        "pos_x": 10,
        "pos_y": 20,
        "pos_z": 100,
        "velocity": 300,
        "fuel": 500,
        "tunnel": [(0, 4000)],
        "command": "landing_finish",
    }

    # Tworzenie obiektu Database i wywołanie metody
    db = Database()
    db.add_data_plane(data)

    # Weryfikacja, że wykonano zapytanie SQL z oczekiwanymi wartościami
    mock_cursor.execute.assert_called_once_with(
        ADD_DATA_PLANE,
        (1, 10, 20, 100, 300, 500, 1, True, False)
    )
@patch('psycopg2.connect')
def test_get_points(mock_connect):
    # Mockowanie połączenia i kursora
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_connect.return_value = mock_conn
    mock_conn.cursor.return_value.__enter__.return_value = mock_cursor

    # Dane zwrócone przez zapytanie
    mock_cursor.fetchall.return_value = [(10, 20, 30)]

    # Tworzenie obiektu Database i wywołanie metody
    db = Database()
    result = db.get_points(1)

    # Weryfikacja, że wykonano odpowiednie zapytanie SQL
    mock_cursor.execute.assert_called_once_with(SELECT_POINTS_BY_NUMBER_FLIGHT, (1,))
    # Weryfikacja zwróconych danych
    assert result == [(10, 20, 30)]


@patch('psycopg2.connect')
def test_update_crash_plane(mock_connect):
    # Mockowanie połączenia i kursora
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_connect.return_value = mock_conn
    mock_conn.cursor.return_value.__enter__.return_value = mock_cursor

    # Tworzenie obiektu Database i wywołanie metody
    db = Database()
    db.update_crash_plane(5)

    # Weryfikacja, że wykonano odpowiednie zapytanie SQL
    mock_cursor.execute.assert_called_once_with(UPDATE_CRASH, (5,))


@patch('psycopg2.connect')
def test_connection_management(mock_connect):
    # Mockowanie połączenia
    mock_conn = MagicMock()
    mock_connect.return_value = mock_conn

    # Tworzenie obiektu Database
    db = Database()

    # Pobieranie połączenia
    conn = db.get_connection()
    assert conn == mock_conn

    # Zwalnianie połączenia
    db.release_connection(conn)

    # Weryfikacja, że połączenie zostało ponownie dodane do kolejki
    assert db.queue.qsize() == db.min_connections


@patch('psycopg2.connect')
def test_select_crash_state(mock_connect):
    # Mockowanie połączenia i kursora
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_connect.return_value = mock_conn
    mock_conn.cursor.return_value.__enter__.return_value = mock_cursor

    # Dane zwrócone przez zapytanie
    mock_cursor.fetchall.return_value = [(True,)]

    # Tworzenie obiektu Database i wywołanie metody
    db = Database()
    result = db.select_crash_state({"number_flight": 1})

    # Weryfikacja, że wykonano odpowiednie zapytanie SQL
    mock_cursor.execute.assert_called_once_with(SELECT_CRASH_STATE, (1,))
    # Weryfikacja zwróconych danych
    assert result is True
