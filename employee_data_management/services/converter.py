class Converter:
    @staticmethod
    def request_to_internal_3(data):
        """
        transformation BIAN -> no BIAN
        """
        internal_data = {
            "documentType": data["PersonIdentification"]["TypeOfIdentification"],
            "documentNumber": data["PersonIdentification"]["IdentityCardNumber"]
        }
        return internal_data

    @staticmethod
    def internal_to_response_3(internal_data):
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
    
    @staticmethod
    def request_to_internal_1(data):
        """
        transformation BIAN -> no BIAN
        """
        internal_data = {
            "tipo_documento": data["PersonIdentification"]["TypeOfIdentification"],
            "numero_documento": data["PersonIdentification"]["IdentityCardNumber"]
        }
        return internal_data

    @staticmethod
    def internal_to_response_1(internal_data):
        """
        transformation no BIAN -> BIAN
        """
        response_data = {
            "Account": {
                "Identification": internal_data.get("id_cuenta", ""),
                "BaseCurrency": internal_data.get("tipo_moneda", "")
            }
        }
        return response_data
    
    @staticmethod
    def request_to_internal_2(data):
        """
        transformation BIAN -> no BIAN
        """
        internal_data = {
            "numero_cuenta": data["Account"]["Identification"]
        }
        return internal_data

    @staticmethod
    def internal_to_response_2(internal_data):
        """
        transformation no BIAN -> BIAN
        """
        response_data = {
            "Account": {
                "Identification": internal_data.get("numero_cuenta", ""),
                "BaseCurrency": internal_data.get("tipo_moneda_cuenta", ""),
                "Status": internal_data.get("estado_cuenta", ""),
                "Type": internal_data.get("tipo_cuenta", "")
            }
        }
        return response_data