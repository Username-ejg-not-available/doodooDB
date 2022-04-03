#!/usr/bin/env python3
import parser.lex as lex

lex.rules = [
	{'regex': 'SELECT|select', 'action': 'SELECT', 'dfa': {'startState': 0, 'sigma': ['S', 'E', 'L', 'C', 'T', 's', 'e', 'l', 'c', 't'], 'finStates': [6, 12], 'deltaT': [[1, None, None, None, None, 7, None, None, None, None], [None, 2, None, None, None, None, None, None, None, None], [None, None, 3, None, None, None, None, None, None, None], [None, 4, None, None, None, None, None, None, None, None], [None, None, None, 5, None, None, None, None, None, None], [None, None, None, None, 6, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, 8, None, None, None], [None, None, None, None, None, None, None, 9, None, None], [None, None, None, None, None, None, 10, None, None, None], [None, None, None, None, None, None, None, None, 11, None], [None, None, None, None, None, None, None, None, None, 12], [None, None, None, None, None, None, None, None, None, None]]}},
	{'regex': 'FROM|from', 'action': 'FROM', 'dfa': {'startState': 0, 'sigma': ['F', 'R', 'O', 'M', 'f', 'r', 'o', 'm'], 'finStates': [4, 8], 'deltaT': [[1, None, None, None, 5, None, None, None], [None, 2, None, None, None, None, None, None], [None, None, 3, None, None, None, None, None], [None, None, None, 4, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, 6, None, None], [None, None, None, None, None, None, 7, None], [None, None, None, None, None, None, None, 8], [None, None, None, None, None, None, None, None]]}},
	{'regex': 'WHERE|where', 'action': 'WHERE', 'dfa': {'startState': 0, 'sigma': ['W', 'H', 'E', 'R', 'w', 'h', 'e', 'r'], 'finStates': [5, 10], 'deltaT': [[1, None, None, None, 6, None, None, None], [None, 2, None, None, None, None, None, None], [None, None, 3, None, None, None, None, None], [None, None, None, 4, None, None, None, None], [None, None, 5, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, 7, None, None], [None, None, None, None, None, None, 8, None], [None, None, None, None, None, None, None, 9], [None, None, None, None, None, None, 10, None], [None, None, None, None, None, None, None, None]]}},
	{'regex': 'TABLE|table', 'action': 'TABLE', 'dfa': {'startState': 0, 'sigma': ['T', 'A', 'B', 'L', 'E', 't', 'a', 'b', 'l', 'e'], 'finStates': [5, 10], 'deltaT': [[1, None, None, None, None, 6, None, None, None, None], [None, 2, None, None, None, None, None, None, None, None], [None, None, 3, None, None, None, None, None, None, None], [None, None, None, 4, None, None, None, None, None, None], [None, None, None, None, 5, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, 7, None, None, None], [None, None, None, None, None, None, None, 8, None, None], [None, None, None, None, None, None, None, None, 9, None], [None, None, None, None, None, None, None, None, None, 10], [None, None, None, None, None, None, None, None, None, None]]}},
	{'regex': 'ALTER|alter', 'action': 'ALTER', 'dfa': {'startState': 0, 'sigma': ['A', 'L', 'T', 'E', 'R', 'a', 'l', 't', 'e', 'r'], 'finStates': [5, 10], 'deltaT': [[1, None, None, None, None, 6, None, None, None, None], [None, 2, None, None, None, None, None, None, None, None], [None, None, 3, None, None, None, None, None, None, None], [None, None, None, 4, None, None, None, None, None, None], [None, None, None, None, 5, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, 7, None, None, None], [None, None, None, None, None, None, None, 8, None, None], [None, None, None, None, None, None, None, None, 9, None], [None, None, None, None, None, None, None, None, None, 10], [None, None, None, None, None, None, None, None, None, None]]}},
	{'regex': 'ADD|add', 'action': 'ADD', 'dfa': {'startState': 0, 'sigma': ['A', 'D', 'a', 'd'], 'finStates': [3, 6], 'deltaT': [[1, None, 4, None], [None, 2, None, None], [None, 3, None, None], [None, None, None, None], [None, None, None, 5], [None, None, None, 6], [None, None, None, None]]}},
	{'regex': 'DROP|drop', 'action': 'DROP', 'dfa': {'startState': 0, 'sigma': ['D', 'R', 'O', 'P', 'd', 'r', 'o', 'p'], 'finStates': [4, 8], 'deltaT': [[1, None, None, None, 5, None, None, None], [None, 2, None, None, None, None, None, None], [None, None, 3, None, None, None, None, None], [None, None, None, 4, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, 6, None, None], [None, None, None, None, None, None, 7, None], [None, None, None, None, None, None, None, 8], [None, None, None, None, None, None, None, None]]}},
	{'regex': 'TRUNCATE|truncate', 'action': 'TRUNCATE', 'dfa': {'startState': 0, 'sigma': ['T', 'R', 'U', 'N', 'C', 'A', 'E', 't', 'r', 'u', 'n', 'c', 'a', 'e'], 'finStates': [8, 16], 'deltaT': [[1, None, None, None, None, None, None, 9, None, None, None, None, None, None], [None, 2, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, 3, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, 4, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, 5, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, 6, None, None, None, None, None, None, None, None], [7, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, 8, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, 10, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, 11, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, 12, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, 13, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, 14, None], [None, None, None, None, None, None, None, 15, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, 16], [None, None, None, None, None, None, None, None, None, None, None, None, None, None]]}},
	{'regex': 'CREATE|create', 'action': 'CREATE', 'dfa': {'startState': 0, 'sigma': ['C', 'R', 'E', 'A', 'T', 'c', 'r', 'e', 'a', 't'], 'finStates': [6, 12], 'deltaT': [[1, None, None, None, None, 7, None, None, None, None], [None, 2, None, None, None, None, None, None, None, None], [None, None, 3, None, None, None, None, None, None, None], [None, None, None, 4, None, None, None, None, None, None], [None, None, None, None, 5, None, None, None, None, None], [None, None, 6, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, 8, None, None, None], [None, None, None, None, None, None, None, 9, None, None], [None, None, None, None, None, None, None, None, 10, None], [None, None, None, None, None, None, None, None, None, 11], [None, None, None, None, None, None, None, 12, None, None], [None, None, None, None, None, None, None, None, None, None]]}},
	{'regex': 'INSERT\\_INTO|insert\\_into', 'action': 'INSERT', 'dfa': {'startState': 0, 'sigma': ['I', 'N', 'S', 'E', 'R', 'T', ' ', 'O', 'i', 'n', 's', 'e', 'r', 't', 'o'], 'finStates': [11, 22], 'deltaT': [[1, None, None, None, None, None, None, None, 12, None, None, None, None, None, None], [None, 2, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, 3, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, 4, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, 5, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, 6, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, 7, None, None, None, None, None, None, None, None], [8, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, 9, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, 10, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, 11, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, 13, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, 14, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, 15, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, 16, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, 17, None], [None, None, None, None, None, None, 18, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, 19, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, 20, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, 21, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, 22], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]]}},
	{'regex': 'VALUES|values', 'action': 'VALUES', 'dfa': {'startState': 0, 'sigma': ['V', 'A', 'L', 'U', 'E', 'S', 'v', 'a', 'l', 'u', 'e', 's'], 'finStates': [6, 12], 'deltaT': [[1, None, None, None, None, None, 7, None, None, None, None, None], [None, 2, None, None, None, None, None, None, None, None, None, None], [None, None, 3, None, None, None, None, None, None, None, None, None], [None, None, None, 4, None, None, None, None, None, None, None, None], [None, None, None, None, 5, None, None, None, None, None, None, None], [None, None, None, None, None, 6, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, 8, None, None, None, None], [None, None, None, None, None, None, None, None, 9, None, None, None], [None, None, None, None, None, None, None, None, None, 10, None, None], [None, None, None, None, None, None, None, None, None, None, 11, None], [None, None, None, None, None, None, None, None, None, None, None, 12], [None, None, None, None, None, None, None, None, None, None, None, None]]}},
	{'regex': '(NATURAL\\_JOIN|natural\\_join)', 'action': 'NATJOIN', 'dfa': {'startState': 0, 'sigma': ['N', 'A', 'T', 'U', 'R', 'L', ' ', 'J', 'O', 'I', 'n', 'a', 't', 'u', 'r', 'l', 'j', 'o', 'i'], 'finStates': [12, 24], 'deltaT': [[1, None, None, None, None, None, None, None, None, None, 13, None, None, None, None, None, None, None, None], [None, 2, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, 3, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, 4, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, 5, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, 6, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, 7, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, 8, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, 9, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, 10, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, 11, None, None, None, None, None, None, None, None, None], [12, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, 14, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, 15, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, 16, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, 17, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, 18, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 19, None, None, None], [None, None, None, None, None, None, 20, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 21, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 22, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 23], [None, None, None, None, None, None, None, None, None, None, 24, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]]}},
	{'regex': '(INNER\\_JOIN|inner\\_join)', 'action': 'INNERJOIN', 'dfa': {'startState': 0, 'sigma': ['I', 'N', 'E', 'R', ' ', 'J', 'O', 'i', 'n', 'e', 'r', 'j', 'o'], 'finStates': [10, 20], 'deltaT': [[1, None, None, None, None, None, None, 11, None, None, None, None, None], [None, 2, None, None, None, None, None, None, None, None, None, None, None], [None, 3, None, None, None, None, None, None, None, None, None, None, None], [None, None, 4, None, None, None, None, None, None, None, None, None, None], [None, None, None, 5, None, None, None, None, None, None, None, None, None], [None, None, None, None, 6, None, None, None, None, None, None, None, None], [None, None, None, None, None, 7, None, None, None, None, None, None, None], [None, None, None, None, None, None, 8, None, None, None, None, None, None], [9, None, None, None, None, None, None, None, None, None, None, None, None], [None, 10, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, 12, None, None, None, None], [None, None, None, None, None, None, None, None, 13, None, None, None, None], [None, None, None, None, None, None, None, None, None, 14, None, None, None], [None, None, None, None, None, None, None, None, None, None, 15, None, None], [None, None, None, None, 16, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, 17, None], [None, None, None, None, None, None, None, None, None, None, None, None, 18], [None, None, None, None, None, None, None, 19, None, None, None, None, None], [None, None, None, None, None, None, None, None, 20, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None]]}},
	{'regex': 'DISTINCT|distinct', 'action': 'DISTINCT', 'dfa': {'startState': 0, 'sigma': ['D', 'I', 'S', 'T', 'N', 'C', 'd', 'i', 's', 't', 'n', 'c'], 'finStates': [8, 16], 'deltaT': [[1, None, None, None, None, None, 9, None, None, None, None, None], [None, 2, None, None, None, None, None, None, None, None, None, None], [None, None, 3, None, None, None, None, None, None, None, None, None], [None, None, None, 4, None, None, None, None, None, None, None, None], [None, 5, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, 6, None, None, None, None, None, None, None], [None, None, None, None, None, 7, None, None, None, None, None, None], [None, None, None, 8, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, 10, None, None, None, None], [None, None, None, None, None, None, None, None, 11, None, None, None], [None, None, None, None, None, None, None, None, None, 12, None, None], [None, None, None, None, None, None, None, 13, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, 14, None], [None, None, None, None, None, None, None, None, None, None, None, 15], [None, None, None, None, None, None, None, None, None, 16, None, None], [None, None, None, None, None, None, None, None, None, None, None, None]]}},
	{'regex': 'AS|as', 'action': 'AS', 'dfa': {'startState': 0, 'sigma': ['A', 'S', 'a', 's'], 'finStates': [2, 4], 'deltaT': [[1, None, 3, None], [None, 2, None, None], [None, None, None, None], [None, None, None, 4], [None, None, None, None]]}},
	{'regex': 'ON|on', 'action': 'ON', 'dfa': {'startState': 0, 'sigma': ['O', 'N', 'o', 'n'], 'finStates': [2, 4], 'deltaT': [[1, None, 3, None], [None, 2, None, None], [None, None, None, None], [None, None, None, 4], [None, None, None, None]]}},
	{'regex': 'NULL', 'action': 'NULL', 'dfa': {'startState': 0, 'sigma': ['N', 'U', 'L'], 'finStates': [4], 'deltaT': [[1, None, None], [None, 2, None], [None, None, 3], [None, None, 4], [None, None, None]]}},
	{'regex': 'PRIMARY\\_KEY', 'action': 'PRIMARYKEY', 'dfa': {'startState': 0, 'sigma': ['P', 'R', 'I', 'M', 'A', 'Y', ' ', 'K', 'E'], 'finStates': [11], 'deltaT': [[1, None, None, None, None, None, None, None, None], [None, 2, None, None, None, None, None, None, None], [None, None, 3, None, None, None, None, None, None], [None, None, None, 4, None, None, None, None, None], [None, None, None, None, 5, None, None, None, None], [None, 6, None, None, None, None, None, None, None], [None, None, None, None, None, 7, None, None, None], [None, None, None, None, None, None, 8, None, None], [None, None, None, None, None, None, None, 9, None], [None, None, None, None, None, None, None, None, 10], [None, None, None, None, None, 11, None, None, None], [None, None, None, None, None, None, None, None, None]]}},
	{'regex': 'AUTO_INCREMENT', 'action': 'AUTOINC', 'dfa': {'startState': 0, 'sigma': ['A', 'U', 'T', 'O', '_', 'I', 'N', 'C', 'R', 'E', 'M'], 'finStates': [14], 'deltaT': [[1, None, None, None, None, None, None, None, None, None, None], [None, 2, None, None, None, None, None, None, None, None, None], [None, None, 3, None, None, None, None, None, None, None, None], [None, None, None, 4, None, None, None, None, None, None, None], [None, None, None, None, 5, None, None, None, None, None, None], [None, None, None, None, None, 6, None, None, None, None, None], [None, None, None, None, None, None, 7, None, None, None, None], [None, None, None, None, None, None, None, 8, None, None, None], [None, None, None, None, None, None, None, None, 9, None, None], [None, None, None, None, None, None, None, None, None, 10, None], [None, None, None, None, None, None, None, None, None, None, 11], [None, None, None, None, None, None, None, None, None, 12, None], [None, None, None, None, None, None, 13, None, None, None, None], [None, None, 14, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None]]}},
	{'regex': 'INT|int|INTEGER|integer', 'action': 'INTTYPE', 'dfa': {'startState': 0, 'sigma': ['I', 'N', 'T', 'i', 'n', 't', 'E', 'G', 'R', 'e', 'g', 'r'], 'finStates': [3, 6], 'deltaT': [[1, None, None, 4, None, None, None, None, None, None, None, None], [None, 2, None, None, None, None, None, None, None, None, None, None], [None, None, 3, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, 5, None, None, None, None, None, None, None], [None, None, None, None, None, 6, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None]]}},
	{'regex': 'VARCHAR|varchar', 'action': 'STRINGTYPE', 'dfa': {'startState': 0, 'sigma': ['V', 'A', 'R', 'C', 'H', 'v', 'a', 'r', 'c', 'h'], 'finStates': [7, 14], 'deltaT': [[1, None, None, None, None, 8, None, None, None, None], [None, 2, None, None, None, None, None, None, None, None], [None, None, 3, None, None, None, None, None, None, None], [None, None, None, 4, None, None, None, None, None, None], [None, None, None, None, 5, None, None, None, None, None], [None, 6, None, None, None, None, None, None, None, None], [None, None, 7, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, 9, None, None, None], [None, None, None, None, None, None, None, 10, None, None], [None, None, None, None, None, None, None, None, 11, None], [None, None, None, None, None, None, None, None, None, 12], [None, None, None, None, None, None, 13, None, None, None], [None, None, None, None, None, None, None, 14, None, None], [None, None, None, None, None, None, None, None, None, None]]}},
	{'regex': 'DATETIME|datetime', 'action': 'DATETIMETYPE', 'dfa': {'startState': 0, 'sigma': ['D', 'A', 'T', 'E', 'I', 'M', 'd', 'a', 't', 'e', 'i', 'm'], 'finStates': [8, 16], 'deltaT': [[1, None, None, None, None, None, 9, None, None, None, None, None], [None, 2, None, None, None, None, None, None, None, None, None, None], [None, None, 3, None, None, None, None, None, None, None, None, None], [None, None, None, 4, None, None, None, None, None, None, None, None], [None, None, 5, None, None, None, None, None, None, None, None, None], [None, None, None, None, 6, None, None, None, None, None, None, None], [None, None, None, None, None, 7, None, None, None, None, None, None], [None, None, None, 8, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, 10, None, None, None, None], [None, None, None, None, None, None, None, None, 11, None, None, None], [None, None, None, None, None, None, None, None, None, 12, None, None], [None, None, None, None, None, None, None, None, 13, None, None, None], [None, None, None, None, None, None, None, None, None, None, 14, None], [None, None, None, None, None, None, None, None, None, None, None, 15], [None, None, None, None, None, None, None, None, None, 16, None, None], [None, None, None, None, None, None, None, None, None, None, None, None]]}},
	{'regex': 'BOOL|bool|BOOLEAN|boolean', 'action': 'BOOLTYPE', 'dfa': {'startState': 0, 'sigma': ['B', 'O', 'L', 'b', 'o', 'l', 'E', 'A', 'N', 'e', 'a', 'n'], 'finStates': [4, 8], 'deltaT': [[1, None, None, 5, None, None, None, None, None, None, None, None], [None, 2, None, None, None, None, None, None, None, None, None, None], [None, 3, None, None, None, None, None, None, None, None, None, None], [None, None, 4, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, 6, None, None, None, None, None, None, None], [None, None, None, None, 7, None, None, None, None, None, None, None], [None, None, None, None, None, 8, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None]]}},
	{'regex': 'FLOAT|float', 'action': 'FLOATTYPE', 'dfa': {'startState': 0, 'sigma': ['F', 'L', 'O', 'A', 'T', 'f', 'l', 'o', 'a', 't'], 'finStates': [5, 10], 'deltaT': [[1, None, None, None, None, 6, None, None, None, None], [None, 2, None, None, None, None, None, None, None, None], [None, None, 3, None, None, None, None, None, None, None], [None, None, None, 4, None, None, None, None, None, None], [None, None, None, None, 5, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, 7, None, None, None], [None, None, None, None, None, None, None, 8, None, None], [None, None, None, None, None, None, None, None, 9, None], [None, None, None, None, None, None, None, None, None, 10], [None, None, None, None, None, None, None, None, None, None]]}},
	{'regex': "'([^']|(\\\\'))*'", 'action': 'STRING', 'dfa': {'startState': 0, 'sigma': ["'", '^', 'z', '#', 'h', '6', '(', '*', '1', ' ', 'S', 'D', '}', 'L', '%', 'y', '\\', 'P', '\n', '!', 'l', 'H', '~', 'q', '?', 'T', 'j', '|', 'G', 'b', ']', '{', '_', '+', 'E', 'C', 'R', 'g', '>', '8', ',', 's', 'Y', 'Q', 'x', 'n', '"', '5', '9', '7', '@', '4', 'M', '$', 'U', '-', ':', 'X', 'F', 'O', '[', 'c', '\t', 'r', 'w', '0', ')', '<', 'W', 'A', '=', 'Z', 'p', 'o', ';', 'k', '`', 't', 'V', 'B', 'm', '3', 'J', '/', 'u', '&', '2', 'v', 'd', 'N', 'K', '.', 'a', 'e', 'f', 'I', 'i'], 'finStates': [2], 'deltaT': [[1, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]]}},
	{'regex': 'TRUE|true|FALSE|false', 'action': 'BOOL', 'dfa': {'startState': 0, 'sigma': ['T', 'R', 'U', 'E', 't', 'r', 'u', 'e', 'F', 'A', 'L', 'S', 'f', 'a', 'l', 's'], 'finStates': [4, 8, 13, 18], 'deltaT': [[1, None, None, None, 5, None, None, None, 9, None, None, None, 14, None, None, None], [None, 2, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, 3, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, 4, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, 6, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, 7, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, 8, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, 10, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, 11, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, 12, None, None, None, None], [None, None, None, 13, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, 15, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, 16, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 17], [None, None, None, None, None, None, None, 18, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]]}},
	{'regex': '[0-9]+', 'action': 'INT', 'dfa': {'startState': 0, 'sigma': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 'finStates': [1, 2], 'deltaT': [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]}},
	{'regex': '[0-9]+(\\.[0-9]+)?', 'action': 'FLOAT', 'dfa': {'startState': 0, 'sigma': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'], 'finStates': [1, 2, 4, 5], 'deltaT': [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, None], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3], [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, None], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, None], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, None]]}},
	{'regex': ',', 'action': 'COMMA', 'dfa': {'startState': 0, 'sigma': [','], 'finStates': [1], 'deltaT': [[1], [None]]}},
	{'regex': '\\*', 'action': 'WILDCARD', 'dfa': {'startState': 0, 'sigma': ['*'], 'finStates': [1], 'deltaT': [[1], [None]]}},
	{'regex': ';', 'action': 'SEMICOLON', 'dfa': {'startState': 0, 'sigma': [';'], 'finStates': [1], 'deltaT': [[1], [None]]}},
	{'regex': '>', 'action': 'GREATER', 'dfa': {'startState': 0, 'sigma': ['>'], 'finStates': [1], 'deltaT': [[1], [None]]}},
	{'regex': '>=', 'action': 'GREATEREQ', 'dfa': {'startState': 0, 'sigma': ['>', '='], 'finStates': [2], 'deltaT': [[1, None], [None, 2], [None, None]]}},
	{'regex': '<', 'action': 'LESS', 'dfa': {'startState': 0, 'sigma': ['<'], 'finStates': [1], 'deltaT': [[1], [None]]}},
	{'regex': '<=', 'action': 'LESSEQ', 'dfa': {'startState': 0, 'sigma': ['<', '='], 'finStates': [2], 'deltaT': [[1, None], [None, 2], [None, None]]}},
	{'regex': '\\+', 'action': 'PLUS', 'dfa': {'startState': 0, 'sigma': ['+'], 'finStates': [1], 'deltaT': [[1], [None]]}},
	{'regex': '\\-', 'action': 'MINUS', 'dfa': {'startState': 0, 'sigma': ['-'], 'finStates': [1], 'deltaT': [[1], [None]]}},
	{'regex': '\\*\\*', 'action': 'EXPONENT', 'dfa': {'startState': 0, 'sigma': ['*'], 'finStates': [2], 'deltaT': [[1], [2], [None]]}},
	{'regex': '/', 'action': 'DIVIDE', 'dfa': {'startState': 0, 'sigma': ['/'], 'finStates': [1], 'deltaT': [[1], [None]]}},
	{'regex': '=', 'action': 'EQUALS', 'dfa': {'startState': 0, 'sigma': ['='], 'finStates': [1], 'deltaT': [[1], [None]]}},
	{'regex': '<>', 'action': 'NEQUALS', 'dfa': {'startState': 0, 'sigma': ['<', '>'], 'finStates': [2], 'deltaT': [[1, None], [None, 2], [None, None]]}},
	{'regex': '\\(', 'action': 'LPAREN', 'dfa': {'startState': 0, 'sigma': ['('], 'finStates': [1], 'deltaT': [[1], [None]]}},
	{'regex': '\\)', 'action': 'RPAREN', 'dfa': {'startState': 0, 'sigma': [')'], 'finStates': [1], 'deltaT': [[1], [None]]}},
	{'regex': 'AND|and', 'action': 'AND', 'dfa': {'startState': 0, 'sigma': ['A', 'N', 'D', 'a', 'n', 'd'], 'finStates': [3, 6], 'deltaT': [[1, None, None, 4, None, None], [None, 2, None, None, None, None], [None, None, 3, None, None, None], [None, None, None, None, None, None], [None, None, None, None, 5, None], [None, None, None, None, None, 6], [None, None, None, None, None, None]]}},
	{'regex': 'OR|or', 'action': 'OR', 'dfa': {'startState': 0, 'sigma': ['O', 'R', 'o', 'r'], 'finStates': [2, 4], 'deltaT': [[1, None, 3, None], [None, 2, None, None], [None, None, None, None], [None, None, None, 4], [None, None, None, None]]}},
	{'regex': 'NOT|not', 'action': 'NOT', 'dfa': {'startState': 0, 'sigma': ['N', 'O', 'T', 'n', 'o', 't'], 'finStates': [3, 6], 'deltaT': [[1, None, None, 4, None, None], [None, 2, None, None, None, None], [None, None, 3, None, None, None], [None, None, None, None, None, None], [None, None, None, None, 5, None], [None, None, None, None, None, 6], [None, None, None, None, None, None]]}},
	{'regex': '[_a-zA-Z][\\._a-zA-Z0-9]*', 'action': 'ID', 'dfa': {'startState': 0, 'sigma': ['_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 'finStates': [1, 2], 'deltaT': [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, None, None, None, None, None, None, None, None, None, None, None], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]}},
	{'regex': '[\\_\\n]', 'action': '(SKIP)', 'dfa': {'startState': 0, 'sigma': [' ', '\n'], 'finStates': [1], 'deltaT': [[1, 1], [None, None]]}},
	{'regex': '.', 'action': '(ERR) "Bad token"', 'dfa': {'startState': 0, 'sigma': ['\t', '~', '}', '|', '{', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', '`', '_', '^', ']', '\\', '[', 'Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A', '@', '?', '>', '=', '<', ';', ':', '9', '8', '7', '6', '5', '4', '3', '2', '1', '0', '/', '.', '-', ',', '+', '*', ')', '(', "'", '&', '%', '$', '#', '"', '!', ' '], 'finStates': [1], 'deltaT': [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]]}},
]
