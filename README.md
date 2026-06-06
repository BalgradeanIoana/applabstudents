# Student Laboratory Management System

An interactive, object-oriented Command Line Interface (CLI) application built in Python designed to manage students, laboratory assignments, and grading.

## 🛠️ Architecture & Structural Design

The project is built following **Layered Architecture** principles to ensure loose coupling, clean organization, and maintainability:

*   **Domain Layer**: Defines core business entities (`Student`, `Laborator`, `Nota`) and leverages a shared `BaseEntity`. Includes strict component validation using custom business logic validators (`StudentValidator`, `LabValidator`, `NotaValidator`).
*   **Repository Layer**: Handles persistent data storage. Implements structured data reading/writing to text files with robust error checking (`StudentFileRepository`, `LaboratorFileRepository`, `NotaFileRepository`).
*   **Service Layer**: Encapsulates core application flow and business requirements (adding, updating, deleting data). It also features a complex `ReportsService` used for calculating averages and filtering students (e.g., sorting students by grade, identifying students with failing grades below 5).
*   **UI Layer**: Provides a clean, text-based interactive menu layout (`Consola`) with built-in parameter help systems.

## 🚀 Key Features & Python Concepts Used

*   **Object-Oriented Programming (OOP)**: Comprehensive use of inheritance, private attributes encapsulation (`__`), custom entity identifiers, and custom business exceptions.
*   **Modern Python Features**: Utilizes native `@dataclass`, `@property` attributes, `@staticmethod` converters, and advanced functional programming concepts such as `lambda` functions and `filter` primitives.
*   **Persistence & Validation**: Prevents data corruption through structural integrity testing (such as checking duplicate IDs or catching unexpected user type mismatch values).

## 📂 Project Tree Structure

```text
ro/ubb/applabstudents/
├── domain/       # Entities, custom exceptions, and validators
├── repository/   # Specialized storage arrays and file storage systems
├── service/      # Business logic services and DTO components
└── ui/           # Terminal UI menu systems