# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI, using HTTP methods, request and response data, status codes, and automated tests. You will practice designing endpoints that clients can use predictably.

## 📝 Tasks

### 🛠️ Create and Run Your First Endpoint

#### Description
Install FastAPI with its standard dependencies, run the provided application with Uvicorn, and add a `GET /health` endpoint.

#### Requirements
The completed application must:

- Start with `uvicorn starter_code:app --reload`
- Return `{"status": "ok"}` from `GET /health`
- Return a successful HTTP status code when the endpoint works

### 🛠️ Build Task Resource Endpoints

#### Description
Create a small task API backed by an in-memory dictionary. Define a Pydantic model for task data, then add endpoints for listing, creating, and retrieving tasks.

#### Requirements
The completed API must:

- Define a task model with an integer `id`, a string `title`, and a boolean `completed` field that defaults to `false`
- Implement `GET /tasks`, `POST /tasks`, and `GET /tasks/{task_id}`
- Return HTTP `201` when a task is created and HTTP `404` when a requested task does not exist
- Use FastAPI and Pydantic to validate incoming task data

### 🛠️ Update, Delete, and Test Tasks

#### Description
Complete the resource lifecycle by adding endpoints to update and delete tasks. Write automated tests with FastAPI's `TestClient` to check successful requests and common error cases.

#### Requirements
The completed API must:

- Implement `PUT /tasks/{task_id}` and `DELETE /tasks/{task_id}`
- Return HTTP `404` when updating or deleting a task that does not exist
- Include tests for listing, creating, retrieving, updating, and deleting tasks
- Include tests that verify a missing task returns HTTP `404` and invalid request data is rejected
- Keep tests independent so one test's in-memory data does not affect another test