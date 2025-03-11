#!/usr/bin/env python3

table_num = 0

while table_num <= 10:
    print(f"Table de {table_num}: ", end="")
    
    multiplier = 0
    while multiplier <= 10:
        print(table_num * multiplier, end=" ")
        multiplier += 1
    
    print()  # ขึ้นบรรทัดใหม่
    table_num += 1