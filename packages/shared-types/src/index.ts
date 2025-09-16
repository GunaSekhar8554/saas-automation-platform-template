// Placeholder for shared types - will be expanded based on backend models
export interface User {
  id: string;
  email: string;
  name: string;
}

export interface Tenant {
  id: string;
  name: string;
}

export interface Migration {
  id: string;
  name: string;
  status: 'pending' | 'running' | 'completed' | 'failed';
}

export interface Agent {
  id: string;
  type: string;
  status: 'idle' | 'running' | 'error';
}
