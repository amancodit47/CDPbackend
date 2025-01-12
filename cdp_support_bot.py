# from typing import Dict, List
# import logging

# class CDPSupportBot:
#     def __init__(self):
#         self.logger = self._setup_logger()
#         # Enhanced sample responses with detailed content
#         self.sample_responses = {
#             "segment": {
#                 "source": {
#                     "title": "Setting up a Source in Segment",
#                     "content": """To set up a new source in Segment, follow these steps:

# 1. Log in to your Segment workspace
# 2. Click on 'Add Source' in the Sources section
# 3. Choose your source type from the catalog
# 4. Configure your source settings:
#    - Name your source
#    - Select the appropriate data collection method
#    - Configure any source-specific settings
# 5. Get your write key (if applicable)
# 6. Implement the tracking code
# 7. Verify your implementation

# Common source types include:
# - Website (Javascript)
# - Mobile App (iOS/Android)
# - Server (Node.js, Python, etc.)
# - Cloud Apps (Salesforce, Zendesk, etc.)""",
#                     "url": "https://segment.com/docs/connections/sources/"
#                 },
#                 "audience": {
#                     "title": "Creating Audiences in Segment",
#                     "content": """To create an audience in Segment:

# 1. Navigate to the Personas section
# 2. Click 'New Audience'
# 3. Define your audience criteria:
#    - Select traits and behaviors
#    - Set conditions and filters
#    - Choose update frequency
# 4. Preview your audience
# 5. Activate the audience
# 6. Connect to destinations""",
#                     "url": "https://segment.com/docs/personas/"
#                 }
#             },
#             "mparticle": {
#                 "integration": {
#                     "title": "Creating an mParticle Integration",
#                     "content": """Setting up an integration in mParticle:

# 1. Access the Directory
# 2. Select your desired integration
# 3. Configure the integration:
#    - Add credentials
#    - Set up data mapping
#    - Configure filters
# 4. Test the connection
# 5. Activate the integration

# Key considerations:
# - Ensure data formatting matches requirements
# - Set up proper event filtering
# - Configure user identity mapping
# - Test with sample data before going live""",
#                     "url": "https://docs.mparticle.com/integrations/"
#                 }
#             }
#         }

#     def _setup_logger(self):
#         logger = logging.getLogger('CDPSupportBot')
#         logger.setLevel(logging.INFO)
#         handler = logging.StreamHandler()
#         formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#         handler.setFormatter(formatter)
#         logger.addHandler(handler)
#         return logger

#     def _find_relevant_content(self, query: str) -> Dict:
#         """
#         Find the most relevant content based on query keywords
#         """
#         query = query.lower()
        
#         # Check for Segment-related queries
#         if "segment" in query:
#             if "source" in query or "set up" in query:
#                 return {
#                     "status": "success",
#                     "response": {
#                         "text": self.sample_responses["segment"]["source"]["content"],
#                         "additional_info": {
#                             "title": self.sample_responses["segment"]["source"]["title"],
#                             "platform": "Segment",
#                             "url": self.sample_responses["segment"]["source"]["url"]
#                         }
#                     }
#                 }
#             elif "audience" in query:
#                 return {
#                     "status": "success",
#                     "response": {
#                         "text": self.sample_responses["segment"]["audience"]["content"],
#                         "additional_info": {
#                             "title": self.sample_responses["segment"]["audience"]["title"],
#                             "platform": "Segment",
#                             "url": self.sample_responses["segment"]["audience"]["url"]
#                         }
#                     }
#                 }

#         # Check for mParticle-related queries
#         elif "mparticle" in query:
#             return {
#                 "status": "success",
#                 "response": {
#                     "text": self.sample_responses["mparticle"]["integration"]["content"],
#                     "additional_info": {
#                         "title": self.sample_responses["mparticle"]["integration"]["title"],
#                         "platform": "mParticle",
#                         "url": self.sample_responses["mparticle"]["integration"]["url"]
#                     }
#                 }
#             }
        
#         return {
#             "status": "error",
#             "message": "I can only answer questions related to CDP platforms (Segment, mParticle, Lytics, and Zeotap). Could you please rephrase your question to be more specific about the CDP platform you're interested in?"
#         }

#     def answer_question(self, query: str) -> Dict:
#         """
#         Process the question and return a detailed response
#         """
#         try:
#             return self._find_relevant_content(query)
#         except Exception as e:
#             self.logger.error(f"Error processing question: {str(e)}")
#             return {
#                 "status": "error",
#                 "message": "Sorry, I encountered an error processing your question. Please try again."
#             }
from typing import Dict
import logging

class CDPSupportBot:
    def __init__(self):
        self.logger = self._setup_logger()
        # Enhanced sample responses with detailed content
        self.sample_responses = {
            "segment": {
                "source": {
                    "title": "Setting up a Source in Segment",
                    "content": """To set up a new source in Segment, follow these steps:

1. Log in to your Segment workspace
2. Click on 'Add Source' in the Sources section
3. Choose your source type from the catalog
4. Configure your source settings:
   - Name your source
   - Select the appropriate data collection method
   - Configure any source-specific settings
5. Get your write key (if applicable)
6. Implement the tracking code
7. Verify your implementation

Common source types include:
- Website (Javascript)
- Mobile App (iOS/Android)
- Server (Node.js, Python, etc.)
- Cloud Apps (Salesforce, Zendesk, etc.)""",
                    "url": "https://segment.com/docs/connections/sources/"
                },
                "audience": {
                    "title": "Creating Audiences in Segment",
                    "content": """To create an audience in Segment:

1. Navigate to the Personas section
2. Click 'New Audience'
3. Define your audience criteria:
   - Select traits and behaviors
   - Set conditions and filters
   - Choose update frequency
4. Preview your audience
5. Activate the audience
6. Connect to destinations""",
                    "url": "https://segment.com/docs/personas/"
                }
            },
            "mparticle": {
                "integration": {
                    "title": "Creating an mParticle Integration",
                    "content": """Setting up an integration in mParticle:

1. Access the Directory
2. Select your desired integration
3. Configure the integration:
   - Add credentials
   - Set up data mapping
   - Configure filters
4. Test the connection
5. Activate the integration

Key considerations:
- Ensure data formatting matches requirements
- Set up proper event filtering
- Configure user identity mapping
- Test with sample data before going live""",
                    "url": "https://docs.mparticle.com/integrations/"
                }
            },
            "zeotap": {
                "integration": {
                    "title": "Integrating Data with Zeotap",
                    "content": """To integrate your data with Zeotap, follow these steps:

1. Initial Setup
   - Log in to your Zeotap Customer Intelligence (CI) Platform
   - Navigate to the Data Integration section
   - Click on 'New Integration'

2. Choose Integration Method
   - Direct File Upload (CSV, JSON)
   - API Integration
   - SDK Implementation
   - Server-to-Server Integration

3. Configure Data Mapping
   - Define user identifiers (cookies, MAIDs, CRM IDs)
   - Map your data fields to Zeotap's schema
   - Set up data transformation rules if needed
   - Configure update frequency

4. Data Validation
   - Run test data through the integration
   - Verify data format and mapping
   - Check for any data quality issues
   - Validate user identity resolution

5. Activation Steps
   - Set up data refresh schedules
   - Configure data sync frequency
   - Enable real-time data streaming if needed
   - Set up error notifications

6. Monitoring and Maintenance
   - Monitor data flow in real-time
   - Check data quality metrics
   - Set up alerts for integration issues
   - Regular audit of data mapping

Remember to:
- Ensure data compliance with privacy regulations
- Document all integration configurations
- Set up proper error handling
- Monitor data quality regularly""",
                    "url": "https://docs.zeotap.com/home/en-us/"
                }
            }
        }

    def _setup_logger(self):
        logger = logging.getLogger('CDPSupportBot')
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def _find_relevant_content(self, query: str) -> Dict:
        """
        Find the most relevant content based on query keywords
        """
        query = query.lower()
        
        # Check for Segment-related queries
        if "segment" in query:
            if "source" in query or "set up" in query:
                return {
                    "status": "success",
                    "response": {
                        "text": self.sample_responses["segment"]["source"]["content"],
                        "additional_info": {
                            "title": self.sample_responses["segment"]["source"]["title"],
                            "platform": "Segment",
                            "url": self.sample_responses["segment"]["source"]["url"]
                        }
                    }
                }
            elif "audience" in query:
                return {
                    "status": "success",
                    "response": {
                        "text": self.sample_responses["segment"]["audience"]["content"],
                        "additional_info": {
                            "title": self.sample_responses["segment"]["audience"]["title"],
                            "platform": "Segment",
                            "url": self.sample_responses["segment"]["audience"]["url"]
                        }
                    }
                }

        # Check for mParticle-related queries
        elif "mparticle" in query:
            return {
                "status": "success",
                "response": {
                    "text": self.sample_responses["mparticle"]["integration"]["content"],
                    "additional_info": {
                        "title": self.sample_responses["mparticle"]["integration"]["title"],
                        "platform": "mParticle",
                        "url": self.sample_responses["mparticle"]["integration"]["url"]
                    }
                }
            }
        
        # Check for Zeotap-related queries
        elif "zeotap" in query or ("integrate" in query and "data" in query and "zeotap" in query):
            return {
                "status": "success",
                "response": {
                    "text": self.sample_responses["zeotap"]["integration"]["content"],
                    "additional_info": {
                        "title": self.sample_responses["zeotap"]["integration"]["title"],
                        "platform": "Zeotap",
                        "url": self.sample_responses["zeotap"]["integration"]["url"]
                    }
                }
            }
        
        return {
            "status": "error",
            "message": "I can only answer questions related to CDP platforms (Segment, mParticle, Lytics, and Zeotap). Could you please rephrase your question to be more specific about the CDP platform you're interested in?"
        }

    def answer_question(self, query: str) -> Dict:
        """
        Process the question and return a detailed response
        """
        try:
            return self._find_relevant_content(query)
        except Exception as e:
            self.logger.error(f"Error processing question: {str(e)}")
            return {
                "status": "error",
                "message": "Sorry, I encountered an error processing your question. Please try again."
            }
