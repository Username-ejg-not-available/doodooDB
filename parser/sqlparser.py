#!/usr/bin/env python3
import parser.parse as p
import parser.RelAlgeTree as RAT

p.table = {
	"\x19 :=  ● query \x18": {
		"SELECT": "query := SELECT ● idlist FROM idlist",
		"FROM": None,
		"WILDCARD": None,
		"ID": None,
		"COMMA": None,
		"\x18": None,
		"query": "\x19 := query ● \x18",
		"idlist": None,
		"\x19": None,
	},
	"\x19 := query ● \x18": {
		"SELECT": None,
		"FROM": None,
		"WILDCARD": None,
		"ID": None,
		"COMMA": None,
		"\x18": "accept",
		"query": None,
		"idlist": None,
		"\x19": None,
	},
	"query := SELECT ● idlist FROM idlist": {
		"SELECT": None,
		"FROM": None,
		"WILDCARD": "query := SELECT WILDCARD ● FROM idlist",
		"ID": "idlist := ID ● ",
		"COMMA": None,
		"\x18": None,
		"query": None,
		"idlist": "query := SELECT idlist ● FROM idlist",
		"\x19": None,
	},
	"query := SELECT idlist ● FROM idlist": {
		"SELECT": None,
		"FROM": "query := SELECT idlist FROM ● idlist",
		"WILDCARD": None,
		"ID": None,
		"COMMA": "idlist := idlist COMMA ● ID",
		"\x18": None,
		"query": None,
		"idlist": None,
		"\x19": None,
	},
	"query := SELECT idlist FROM ● idlist": {
		"SELECT": None,
		"FROM": None,
		"WILDCARD": None,
		"ID": "idlist := ID ● ",
		"COMMA": None,
		"\x18": None,
		"query": None,
		"idlist": "query := SELECT idlist FROM idlist ● ",
		"\x19": None,
	},
	"query := SELECT idlist FROM idlist ● ": {
		"SELECT": None,
		"FROM": None,
		"WILDCARD": None,
		"ID": None,
		"COMMA": "idlist := idlist COMMA ● ID",
		"\x18": ('query', 4),
		"query": None,
		"idlist": None,
		"\x19": None,
	},
	"idlist := idlist COMMA ● ID": {
		"SELECT": None,
		"FROM": None,
		"WILDCARD": None,
		"ID": "idlist := idlist COMMA ID ● ",
		"COMMA": None,
		"\x18": None,
		"query": None,
		"idlist": None,
		"\x19": None,
	},
	"idlist := idlist COMMA ID ● ": {
		"SELECT": None,
		"FROM": ('idlist', 3),
		"WILDCARD": None,
		"ID": None,
		"COMMA": ('idlist', 3),
		"\x18": ('idlist', 3),
		"query": None,
		"idlist": None,
		"\x19": None,
	},
	"idlist := ID ● ": {
		"SELECT": None,
		"FROM": ('idlist', 1),
		"WILDCARD": None,
		"ID": None,
		"COMMA": ('idlist', 1),
		"\x18": ('idlist', 1),
		"query": None,
		"idlist": None,
		"\x19": None,
	},
	"query := SELECT WILDCARD ● FROM idlist": {
		"SELECT": None,
		"FROM": "query := SELECT WILDCARD FROM ● idlist",
		"WILDCARD": None,
		"ID": None,
		"COMMA": None,
		"\x18": None,
		"query": None,
		"idlist": None,
		"\x19": None,
	},
	"query := SELECT WILDCARD FROM ● idlist": {
		"SELECT": None,
		"FROM": None,
		"WILDCARD": None,
		"ID": "idlist := ID ● ",
		"COMMA": None,
		"\x18": None,
		"query": None,
		"idlist": "query := SELECT WILDCARD FROM idlist ● ",
		"\x19": None,
	},
	"query := SELECT WILDCARD FROM idlist ● ": {
		"SELECT": None,
		"FROM": None,
		"WILDCARD": None,
		"ID": None,
		"COMMA": "idlist := idlist COMMA ● ID",
		"\x18": ('query', 4),
		"query": None,
		"idlist": None,
		"\x19": None,
	},
}
p.start = list(p.table.keys())[0]
def action1():
    p.semstack = [RAT.Projection(p.semstack[1], p.semstack[0])] + p.semstack[2:]

def action2():
    p.semstack = [[p.currentToken]] + p.semstack

def action3():
    p.semstack = [[p.currentToken] + p.semstack[0]] + p.semstack[1:]

p.actions = {
	"query := SELECT idlist FROM idlist ● ": action1,
	"idlist := ID ● ": action2,
	"idlist := idlist COMMA ID ● ": action3,
}
