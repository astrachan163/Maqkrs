// AgentQL API Configuration
export const AGENTQL_API_KEY = 'AIzaSyCLoEe9r3BXR0K3x7zOA7R7BTXPDUpOxO0';
export const AGENTQL_API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent';

// Content Update Settings
export const CONTENT_UPDATE_INTERVAL = '0 1 * * 0'; // Weekly on Sunday at 1 AM
export const SEARCH_BATCH_SIZE = 10;
export const MAX_SEARCH_RESULTS = 3;

// Scraping Sources
export const SCRAPING_SOURCES = {
  RETAIL_WIKI: 'https://retail.fandom.com/wiki/Retail',
  NRF_BLOG: 'https://nrf.com/blog',
  RETAIL_COUNCIL: 'https://www.retailcouncil.org/resources'
};