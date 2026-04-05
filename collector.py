import WDWR
import time

def main():
    start = time.perf_counter()
    
    hollywood = WDWR.Park("Hollywood Studios", WDWR.ParkSlugs.hollywood)
    print(f"Park times are {hollywood.openTime} - {hollywood.closeTime}")
    if hollywood.isParkOpen():
        print(f"Saving {hollywood.name} as a csv")
        hollywood.attractions.archiveToCSV(hollywood.name,hollywood.lastTimeCheck)
    else:
        print(f"{hollywood.name} is closed at {hollywood.closeTime}")

    dak = WDWR.Park("Animal Kingdom", WDWR.ParkSlugs.dak)
    print(f"Park times are {dak.openTime} - {dak.closeTime}")
    if dak.isParkOpen():
        print(f"Saving {dak.name} as a csv")
        dak.attractions.archiveToCSV(dak.name,dak.lastTimeCheck)
    else:
        print(f"{dak.name} is closed at {dak.closeTime}")

    magic = WDWR.Park("Magic Kingdom", WDWR.ParkSlugs.magic)
    print(f"Park times are {magic.openTime} - {magic.closeTime}")
    if magic.isParkOpen():
        print(f"Saving {magic.name} as a csv")
        magic.attractions.archiveToCSV(magic.name,magic.lastTimeCheck)
    else:
        print(f"{magic.name} is closed at {magic.closeTime}")

    epcot = WDWR.Park("EPCOT", WDWR.ParkSlugs.epcot)
    print(f"Park times are {epcot.openTime} - {epcot.closeTime}")
    if epcot.isParkOpen():
        print(f"Saving {epcot.name} as a csv")
        epcot.attractions.archiveToCSV(epcot.name,epcot.lastTimeCheck)
    else:
        print(f"{epcot.name} is closed at {epcot.closeTime}")

    
    end = time.perf_counter()
    print(f"Time taken is {end-start} seconds")

if __name__ == "__main__":
    main()