<div className="flex flex-col items-center p-4">
      {!showForm && (
        <button
          onClick={handleToggleForm}
          className="bg-green-500 text-white px-4 py-2 rounded"
        >
          Show Login Form
        </button>
      )}

      {showForm && (
        <div className="mt-4">
          <input
            type="text"
            placeholder="Enter username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            className="border p-2 mb-2 rounded block"
          />
          <input
            type="password"
            placeholder="Enter password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="border p-2 mb-2 rounded block"
          />
          <button
            onClick={handleSubmit}
            className="bg-blue-500 text-white px-4 py-2 rounded mt-2"
          >
            Submit
          </button>
        </div>
      )}
    </div>
