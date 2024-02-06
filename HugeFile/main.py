from iodatasphere import IODataSphereScraper
from kfac import KforceJobScraper
from apexsystems import JobScraperApexSystems
from thejudgegroup import JudgeJobScraper
from insightglobal import JobScraperInsightGlobal
from yoh import JobScraperYoh
from Brookesource import BrookSourceJobScraper
from huxley import HuxleyJobScraper
from  beacon import BeaconHillJobScraper
from tricom import JobScraperTricom

def main():

    io_datasphere_scraper = IODataSphereScraper(base_folder='.')

    kforce_scraper = KforceJobScraper()
    kforce_scraper.scrape_and_generate_csv()

    apex_systems_scraper = JobScraperApexSystems()
    apex_systems_scraper.scrape_jobs()

    judge_scraper = JudgeJobScraper()
    judge_scraper.scrape_jobs()
    judge_scraper.generate_csv()

    insight_global_scraper = JobScraperInsightGlobal()
    insight_global_scraper.scrape_jobs()

    yoh_scraper = JobScraperYoh()
    yoh_scraper.scrape_jobs()

    brook_source_scraper = BrookSourceJobScraper()
    brook_source_scraper.scrape_jobs()

    huxley_scraper = HuxleyJobScraper()
    huxley_scraper.scrape_and_generate_csv()

    beacon_hill_scraper = BeaconHillJobScraper()
    beacon_hill_scraper.scrape_jobs()

    scraper = JobScraperTricom()
    scraper.scrape_jobs()

if __name__ == "__main__":
    main()