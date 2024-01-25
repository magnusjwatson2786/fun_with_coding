'''https://www.codewars.com/kata/5915686ed2563aa6650000ab'''

def evil_code_medal(user_time, gold, silver, bronze):
    uts=int(user_time.split(":")[0])*3600 + int(user_time.split(":")[1])*60 +int(user_time.split(":")[2])
    gts=int(gold.split(":")[0])*3600 + int(gold.split(":")[1])*60 +int(gold.split(":")[2])    
    sts=int(silver.split(":")[0])*3600 + int(silver.split(":")[1])*60 +int(silver.split(":")[2])    
    bts=int(bronze.split(":")[0])*3600 + int(bronze.split(":")[1])*60 +int(bronze.split(":")[2])
    
    if uts<gts:
        return "Gold"
    if uts<sts:
        return "Silver"
    if uts<bts:
        return "Bronze"
    else:
        return "None"
