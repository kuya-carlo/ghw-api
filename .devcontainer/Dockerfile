# syntax=docker/dockerfile:1
FROM python:3.12-slim

# Set working directory
WORKDIR /usr/src/app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends git zsh curl wget podman podman-docker sudo \
    && rm -rf /var/lib/apt/lists/*

# Install act CLI
RUN curl -L https://github.com/nektos/act/releases/latest/download/act_Linux_x86_64.tar.gz \
    | tar -xz -C /usr/local/bin act \
    && chmod +x /usr/local/bin/act

# Install Oh My Zsh and plugins
RUN git clone --depth=1 https://github.com/ohmyzsh/ohmyzsh.git /root/.oh-my-zsh \
    && git clone --depth=1 https://github.com/zsh-users/zsh-autosuggestions.git /root/.oh-my-zsh/custom/plugins/zsh-autosuggestions \
    && git clone --depth=1 https://github.com/zsh-users/zsh-syntax-highlighting.git /root/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting \
    && git clone --depth=1 https://github.com/romkatv/powerlevel10k.git /root/.oh-my-zsh/custom/themes/powerlevel10k

# Copy custom shell config files
COPY .devcontainer/.zshrc /root/.zshrc
COPY .devcontainer/.p10k.zsh /root/.p10k.zsh

# Install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy source
COPY app ./app

# Expose port
EXPOSE 8000

# Run app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
