import { useState } from 'react'
import './App.css'

// Simple login component for demonstration purposes
// Accepts an email and password, then displays a message
function Login() {
  // Local state for form fields and result message
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [message, setMessage] = useState('')

  // Handle form submission
  const handleSubmit = (e) => {
    e.preventDefault()
    // Basic check: in a real app, you'd validate against a server
    if (email === 'admin@example.com' && password === 'password') {
      setMessage('Login successful!')
    } else {
      setMessage('Invalid credentials.')
    }
  }

  return (
    <div className="form-container">
      <h1>Login</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="email">Email</label>
          <input
            id="email"
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="admin@example.com"
            required
          />
        </div>
        <div>
          <label htmlFor="password">Password</label>
          <input
            id="password"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <button type="submit">Sign In</button>
      </form>
      {/* Conditionally render feedback message */}
      {message && <p>{message}</p>}
    </div>
  )
}

export default Login
