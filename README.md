# Which-IP

This project provides a simple Docker container that returns the public IP address of the client making the request. It can be useful for identifying an IP address for tasks like logging or authorization.

## Features

- Retrieves and displays the public IP address of the user.
- Lightweight Docker container.

## Requirements

- Docker

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/AiglonDore/which-ip.git
   ```
2. Build the Docker image:
   ```bash
   docker build -t which-ip .
   ```
3. Run the container:
   ```bash
   docker run -p 5000:5000 which-ip
   ```
4. Access the service by navigating to:
   ```
   http://localhost:5000
   ```

## License

This project is licensed under the GPL-3.0 License. See the [LICENSE](./LICENSE) file for more details.
