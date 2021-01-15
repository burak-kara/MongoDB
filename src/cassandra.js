const {Client} = require("cassandra-driver");

async function run() {
    const client = new Client({
        cloud: {
            secureConnectBundle: "D:\\projects\\CS550\\PROJECT\\MongoDB\\secure-connect-cs550.zip",
        },
        credentials: {username: "burak", password: "burakkara"},
    });

    await client.connect();

    // Execute a query
    const rs = await client.execute("SELECT * FROM system.local");
    console.log(`Your cluster returned ${rs.rowLength} row(s)`);

    await client.shutdown();
}

// Run the async function
run();
