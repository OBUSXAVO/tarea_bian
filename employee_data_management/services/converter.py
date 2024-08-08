class Converter:
    @staticmethod
    def request_to_internal(data):
        """
        transformation BIAN -> no BIAN
        """
        internal_data = {
            "documentType": data["PersonIdentification"]["TypeOfIdentification"],
            "documentNumber": data["PersonIdentification"]["IdentityCardNumber"]
        }
        return internal_data

    @staticmethod
    def internal_to_response(internal_data):
        """
        transformation no BIAN -> BIAN
        """
        response_data = {
            "PersonIdentification": {
                "TypeOfIdentification": internal_data.get("documentType", ""),
                "IdentityCardNumber": internal_data.get("documentNumber", ""),
                "PersonName": {
                    "GivenName": internal_data.get("given_name", ""),
                    "MiddleName": internal_data.get("middle_name", "")
                },
                "Contact": {
                    "MobilePhoneNumber": internal_data.get("mobile_phone_number", ""),
                    "PersonalEmailAddress": internal_data.get("personal_email_address", "")
                }
            }
        }
        return response_data