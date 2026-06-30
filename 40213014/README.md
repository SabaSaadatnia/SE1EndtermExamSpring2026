# Digital Bank Loan System

A simple Python code structure for a digital bank similar to BluBank.
The system supports loan eligibility based on the average balance of a bank account.

Architecture:
- Presentation/API entry point: `app.py`
- Application/business layer: services and facade
- Domain layer: entities/models
- Infrastructure/data layer: repositories
- Security layer: authentication service

Design patterns:
- Repository Pattern: separates data access from business logic
- Strategy Pattern: separates loan eligibility algorithms
- Facade Pattern: provides one simple interface for the loan request process
