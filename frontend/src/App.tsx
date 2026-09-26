import { useEffect, useState } from 'react'

interface Task {
  id: string
  title: string
  status: string
}

export default function App() {
  const [goal, setGoal] = useState('Launch an AI operations team for internal automation')
  const [tasks, setTasks] = useState<Task[]>([])
  const [status, setStatus] = useState('idle')

  useEffect(() => {
    fetch('http://localhost:8000/organization/summary')
      .then((res) => res.json())
      .then((data) => setStatus(data.status || 'active'))
      .catch(() => setStatus('offline'))
  }, [])

  const handleGeneratePlan = async () => {
    const res = await fetch('http://localhost:8001/agent/plan', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ goal, context: 'Hermes org dashboard' }),
    })

    const data = await res.json()
    setTasks(data.tasks || [])
  }

  return (
    <div className="app-shell">
      <header className="topbar">
        <div>
          <p className="eyebrow">AI Organization</p>
          <h1>Hermes Dashboard</h1>
        </div>
        <span className={`badge ${status}`}>{status}</span>
      </header>

      <section className="panel">
        <label htmlFor="goal">Organization goal</label>
        <textarea
          id="goal"
          value={goal}
          onChange={(e) => setGoal(e.target.value)}
          rows={4}
        />
        <button onClick={handleGeneratePlan}>Generate plan</button>
      </section>

      <section className="panel">
        <h2>Tasks</h2>
        {tasks.length === 0 ? (
          <p>No tasks generated yet.</p>
        ) : (
          <ul className="task-list">
            {tasks.map((task) => (
              <li key={task.id}>
                <strong>{task.title}</strong>
                <span>{task.status}</span>
              </li>
            ))}
          </ul>
        )}
      </section>
    </div>
  )
}
